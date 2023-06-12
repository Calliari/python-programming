#!/usr/bin/env python3

# https://www.guru99.com/date-time-and-datetime-classes-in-python.html

import re
import os
import ast
import sys
import time
import json
import socket
import datetime
import requests
from datetime import datetime, timedelta


def main():
    # ADD THE PATH OF THE PROJECT TO BE CHECK DAYLY ON THE AWS BACKUPS SERVER
    check_bkp_path_array = [
        '/backups_lpayh_check_this_dir',
        '/backups_path/check_this_file.sql',
        ]


# ===================================

    # BIGPANDA INTEGRATION VARIABLES
    bigpanda_endpoint = 'https://api.bigpanda.io/data/v2/alerts'
    bigpanda_application_key = '9999999999999999' # bigpanda channel or slack channel
    bigpanda_bearer_key = '9999999999999999'

    # SLACK INTEGRATION VARIABLE
    slack_endpoint = "https://hooks.slack.com/services/9999999999/88888888888/00000000000"
    slack_channel = '#slack_channel_name'
    hostname = socket.gethostname()
    host_ip = socket.gethostbyname(hostname)
    subject = "The scheduled backup has not taken place for the past 24 hour(s)!"

    # THIS SCRIPT IS CONFIGURED TO RUN AT 3AM (27 H)
    timestamp_now = time.time()
    twenty_four_hours_ago = timestamp_now - 97200


    number_bkp = 0
    bkp_list = []
    del bkp_list[:]
    for ck_bkp in check_bkp_path_array:
        last_data_modification_timestamp = os.path.getmtime(ck_bkp)
        timestamp_diff = timestamp_now - last_data_modification_timestamp
        timestamp_to_datetime = timestamp_diff / 3600

        if last_data_modification_timestamp < twenty_four_hours_ago:
            number_bkp += 1
            bkp_info = "(%i)==> %s Last modified Date & Time: %s timestamp: %i (%.0f hours ago) " % (number_bkp, ck_bkp, time.strftime('%d/%m/%Y - %H:%M:%S', time.gmtime(last_data_modification_timestamp)), last_data_modification_timestamp, timestamp_to_datetime)

            my_test = {'short': 'false','value': ''}
            my_test_1 = {'value': ''+bkp_info+'' ,'short': 'false'}
            my_test_2 = '%s,%s,' % (my_test, my_test_1)
            bkp_list.extend([my_test_2])

    total_number_bkp = number_bkp
    bkp_list_lines = (' '.join(bkp_list))

    # payload for slack notification (aws-bbd_backup) channel
    payload_slack = {
        'channel': slack_channel,
        'username': '%s:%s' % (hostname, host_ip),
        'attachments':[{
            'pretext':subject,
            'fields':[{
                'title':'Last bkp taken over 24H',
                'value': '%i bkps need to be checked!' % (total_number_bkp),
                'short': 'false'
                },
                {
                'title':'Consider to CHECK bkp & date - time details for:',
                'value': '',
                'short': 'false'
                },
                bkp_list_lines
            ],
            'color':'#ff0000'
        }],
        'icon_emoji':':floppy_disk::'
    }

    json_file = '/tmp/payload_slack.json'
    with open(json_file, 'w') as outfile:
        json.dump(payload_slack, outfile, ensure_ascii=False, indent=2)
    outfile.close()

    s = open(json_file).read()
    s = s.replace('"{', '{')
    s = s.replace('},"', '},')
    f = open(json_file, 'w')
    f.write(s)
    f.close()

    # bigpanda notification (bbd-backup) channel
    if total_number_bkp == 0 :
        bkp_status = 'ok'
        print(bkp_status)
    else:
        bkp_status = 'critical'
        print(bkp_status)

    # payload for bigpanda notification posting status to slack (bbd-backups) channel
    headers = {
        'Authorization': 'Bearer %s ' % (bigpanda_bearer_key),
        'Content-type': 'application/json',
        }
    payload_bigpanda = {
        'app_key': '%s' % (bigpanda_application_key),
        'status': '%s' % (bkp_status),
        'host': 'hostname: %s, ip: %s' % (hostname, host_ip),
        'timestamp': int(timestamp_now),
        'check': '%i bkps need to be checked!' % (total_number_bkp),
        'description': '%s' % subject,
        'monit_action':'check slack channel %s for more info' % (slack_channel)
    }

    #  POST API CALL bigpanda
    requests.post(bigpanda_endpoint, data=json.dumps(payload_bigpanda), headers=headers)

    #  POST API CALL slack
    with open(json_file, 'rb') as payload_slack:
        requests.post(slack_endpoint, data=payload_slack)
    payload_slack.close()
    os.remove(json_file)

if __name__ == '__main__':
    main()
