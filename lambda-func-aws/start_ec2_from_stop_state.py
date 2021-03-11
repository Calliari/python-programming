# -*- coding: utf-8 -*-

""" Lambda to start ec2-instance for project ${project_name} """

# for project "${project_name}" 
## replace the '#' with'$' sign on that variable above for project variable --> "#{project_name}" <-- 
## so terraform can get it from the 'variables.tf' 

import boto3
import time
import datetime

# Enter the region your instances are in. Include only the region without specifying Availability Zone; e.g.; 'us-east-1'
region = "${aws_region}" # replace the '#' with'$' sign on this variable --> "#{aws_region}" 
# Enter the tag your instances
tag    = "${tag_backup_server}" # replace the '#' with'$' sign on this variable --> "#{tag_backup_server}" 

ec2 = boto3.resource('ec2', region_name=region)

def lambda_handler(event, context):

	# get instances with "tag"
	instances = ec2.instances.filter(Filters=[{'Name': 'tag:Name', 'Values': [tag]}])

	# loop through the "instances" with specific "tag"
	for instance in instances:
		# print the ID of each instance
		# print instance

		instance_result = str(instance)

		# remove ==> ec2.Instance(id=' <== from instance result
		remove_begining = instance_result.replace("ec2.Instance(id='", "")
		# remove ==> ') <== from instance result
		remove_ending = remove_begining.replace("')", "")
		# get the Instance string only
		instance_id = remove_ending

		# check if the ID is printed without the  "remove_begining" and "remove_ending" parts
		# print instance_id

		# Start the instance based on id
		ec2.instances.filter(InstanceIds=[instance_id]).start()

		#print few details of the instance
		print("\n----------------------------------------------------")
		print("SUCCESS")
		print("Instance private IP: %s " % (instance.private_ip_address))
		print("Started instances ID: %s at %s \n" % (instance.id, datetime.datetime.now().strftime('%H:%M:%S')))
		print("----------------------------------------------------\n")
