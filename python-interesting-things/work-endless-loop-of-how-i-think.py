#! /usr/bin/env python2.7 

import io, sys,time, itertools # for Py2.7 that would be import cStringIO as io


to_do_task = u"""
  - Replay to all emails...
  - Clean up unused AWS resources - costs saving 
  - Increase disk partitions on the DEV and UAT servers
  - Install anti-virus on All on-premiss servers --> 'URGENT'
  - Create a new DEV website for a new project --> 'URGENT'
  - Grant DATABASE access to a new dev trainee --> 'URGENT'
  - Write a new python script to automate the CI/CD pipeline
  - Translate a Groovy code script into python for cross-platform benefits
  - Architecting a better way for the developer to get a dump-prod-databases for local-software lifecycle
  - Re-write Dockerfile code for lightweight Docker images - improvements for containerization
  - Having fun with this code, 'this is not an actual thing on my todo list, it's just me being a software engineer and playing with code... lol :)'
"""

to_do_list_task_time_done = ['09:35', '10:50','11:55', '12:30', '13:45', '14:58', '15:47', '16:00', '17:35', '18:33']


print('My to-do list for today:\n' + to_do_task)

# pause 'sleep' for the tima assigned, print the 'working...' string for the range times assigned, on the same line 'flush'
for i in range(0,7):
   time.sleep(1)
   sys.stdout.write("working... ")
   sys.stdout.flush()

print('\n##################################################################\n')
print('\nMy to-do task list DONE today:\n')

# convert the variable 'to_do_task' into a list so it can be printed one by one
all_tasks = io.StringIO(to_do_task)
# skip the first line which is the 'null'
next(all_tasks) 
# combine the list-array 'to_do_list_task_time_done' with the 'all_tasks' and print the time is was done with the task list
for time_done_task, task in zip(to_do_list_task_time_done, all_tasks):
    print('Done at ' + str(time_done_task) + task)
    time.sleep(2)

# end message 
print("Let's call it a day and get out of here!!!\n")

