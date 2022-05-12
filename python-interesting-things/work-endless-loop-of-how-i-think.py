#! /usr/bin/env python2.7 
import sys, io, time, itertools # for Py2.7 that would be import cStringIO as io


to_do_task = u"""
    - Clean up unused AWS resources - saving costs
    - Increase disk partitions on the DEV and UAT servers
    - Install anti-virus on All on-premiss servers --> 'URGENT'
    - Create a new DEV website for a new project --> 'URGENT'
    - Grant DATABASE access to a new dev trainee --> 'URGENT'
    - Write a new python script to automate the CI/CD pipeline
    - Translate a bash script into python for cross-platform benefits
    - Architecting a better way for the developer to get a dump-prod-databases for local-software lifecycle
    - Re-write Dockerfile for lightweight Docker images - improvements for containerization
"""

to_do_list_task_time_done = ['10:00', '11:00', '12:00', '13:00', '14:00', '15:00', '16:00', '17:00', '18:00', '19:00']

def to_do_list_today():
    # print('\n clean up AWS acc\n')
    print('My to-do list for today:\n' + to_do_task)

to_do_list_today()

for i in range(0,20):
   time.sleep(1)
   sys.stdout.write("==")
   sys.stdout.flush()

all_tasks = io.StringIO(to_do_task)
print('\nMy to-do task list DONE today:\n')
next(all_tasks)
for time_done_task, task in zip(to_do_list_task_time_done, all_tasks):
    time.sleep(2)
    print('Done at ' + str(time_done_task) + task)
    
    
