#!/usr/bin/env python

"""
A simple python script to list the aws images, 
- keeps the images that are in use on the autoscaling,
- diregister thoses that are more than 2 months,
- but keeps at leat the 3 latest images no matter how old the images are.
"""

import boto3
from datetime import datetime, timedelta
import sys # import module sys to get the type of exception

# define the dry_run_bool(true or false), profile_name, region, ami_tag
# dry_run_bool": 'False'  #--> WARNING: This will really delete the AMI if its set to 'False'
# aws_profile_name = 'project-profile-name-example'
# aws_ami_tag = 'example-webserver'
# aws_snapshot_tag = 'example-webserver'
# aws_region = 'eu-west-2'

# ========== start from here ========== #


aws_projects = { 
    "project-example-1": {
        "dry_run_bool": "False", 
        "aws_region": "eu-west-2",
        "aws_profile_name": "project-1-profile-name-example", 
        "aws_ami_tag": "example-1-webserver", 

        },
    "project-example-2": {
        "dry_run_bool": "False", 
        "aws_region": "eu-west-2",
        "aws_profile_name": "project-2-profile-name-example", 
        "aws_ami_tag": "example-2-webserver", 

        },
}


""" Keep image used by the ASGs """
def images_in_use_func():
    images_in_use = {
        instance.image_id for instance in ec2.instances.all()
    }
    # # show image in use by the ASGs
    # print('\nImages in use \n %s' % (images_in_use))
    return images_in_use


""" Keep images created/built from the past (days) set """
def keep_images_func():
    number_days = 60
    keep_images = set()
    for image in images:
        ## check the images
        # print(image.image_id, image.creation_date, image.tags)

        # getting the created date time from the 'image.creation_date'
        created_at_date = datetime.strptime(image.creation_date, "%Y-%m-%dT%H:%M:%S.000Z", )

        retention_days = datetime.now() - timedelta(number_days)
        if created_at_date > retention_days:
            keep_images.add(image.id)
    # # Keep images created/built from the past (days) set
    # print('\nImages Kept from the past %d days \n %s' % (number_days, keep_images)) 
    return keep_images


""" Keep latest 3 images deployed """
def latest_images_func():
    dict_images = {}
    latest_images = set()
    for image in images:
        ## check the images
        # print(image.image_id, image.creation_date, image.tags)
        # print(image.image_id, image.creation_date)
        dict_images[image.image_id] = image.creation_date 

        # sort by date (newest to oldest)
        ordered_images = sorted(dict_images.items(), key=lambda x:datetime.strptime(x[1], '%Y-%m-%dT%H:%M:%S.000Z'), reverse=True) [:3]
    # getting the images after images sorted 
    for ordered_image in ordered_images:
        latest_images.add(ordered_image[0])
    return latest_images

""" Selected images to keep """
def images_to_keep_func(used_img, keep_img, latest_img):
    # images_to_keep = keep_images | images_in_use | latest_images
    images_to_keep = used_img.union(keep_img, latest_img)
    ## Keep latest 3 images deployed
    # print('\nImages to keep %s' % (images_to_keep)) 
    # print('\nLatest 3 images created/deployed to keep \n %s' % (images_to_keep))
    return images_to_keep

""" Deregister images that are 'older than days set', 'not in use by ags' and 'not the latest 3 deployed' """
def deregister_images_func():
    images_to_keep = images_to_keep_func(images_in_use_func(), keep_images_func(), latest_images_func())
    for image in (image for image in images if image.image_id not in images_to_keep):
        try:
            print('Deregistering: - (%s) Created: - (%s) ' % (image.image_id, image.creation_date))
            # response = image.deregister()
            # print(dry_run_bool)
            response = image.deregister(DryRun=dry_run_bool)
        except Exception as e:
            print(e)
            print("Oops, something went wrong! - Image not DEREGISTERED. Trying to deregistering next image...\n")
        except:
            print("Something else went wrong")
    # print('Image (%s) deregistered from aws-region (%s) aws-acc ()\n' % (image.image_id, aws_region, )) 
    return 'DONE!'


# NOT FINISHED -- Delete snapshot 
# """ Delete snapshot that are 'older than days set * 2'""" 
# def delete_snapshot_func():
#     for snapshot in snapshots:
#         # print('Checking {}'.format(snapshot.id))
#         # print('Checking ',  format(snapshot.id), format(snapshot.start_time))
#         # print('Checking ',  snapshot.id, snapshot.start_time)
#         print('Checking ',  snapshot)
#         snapshot.delete(DryRun=True)
#
# # Delete unattached snapshots
# print('Deleting snapshots.')
# images = [image.id for image in ec2.images.all()]
# for snapshot in ec2.snapshots.filter(OwnerIds=[ACCOUNT_ID]):
#     print('Checking {}'.format(snapshot.id))
#     r = re.match(r".*for (ami-.*) from.*", snapshot.description)
#     if r:
#         if r.groups()[0] not in images:
#             print('Deleting {}'.format(snapshot.id))
#             snapshot.delete()
#
# call the function to test
#print(delete_snapshot_func()) 
# NOT FINISHED -- Delete snapshot 


# End of all functions and start the actions
for key, value in aws_projects.items():
    # print(key, value)
    # print(key, value.items()[0])

    # This is neccessary as python return string boolean as (True), even with ['True', 'true, 'False', 'false' ] from the dict 
    # with this conditional we are converting based on the string ("False" --> False and "false" --> False) the same for ("True" --> True and "true" --> True)
    if value.values()[0] == 'True' or value.values()[0] == 'true':
        dry_run_bool_convert_bool = True
    elif value.values()[0] == 'False' or value.values()[0] == 'true':
         dry_run_bool_convert_bool = False

    # AWS details
    dry_run_bool = dry_run_bool_convert_bool # WARNING: This will really delete the AMI if its set to 'False'
    aws_region = value.values()[1]
    aws_profile_name = value.values()[2]
    aws_ami_tag = value.values()[3]
    # Boto Amazon Web Services (AWS) SDK for Python
    boto3.setup_default_session(profile_name=aws_profile_name)
    ec2 = boto3.resource('ec2', region_name=aws_region)
    images = ec2.images.filter(Owners=['self'], Filters=[{'Name': 'tag:Name', 'Values': [aws_ami_tag]}])
    # snapshots = ec2.snapshots.filter(Filters=[{'Name': 'tag:Name', 'Values': [aws_snapshot_tag]}])


    # print('AWS-Profile-name: [%s] \nAWS-AMI-Tag: [%s] \nAWS-Region: [%s]\ndry_run_bool: [%s]\n' % (aws_profile_name, aws_ami_tag, aws_region, dry_run_bool))
    # print('INFORMATION:\nImages that will NOT be deregistered (img in use) - %s \nImages that will NOT be deregistered (img to keep based on past days specifield) - %s \nImages that will NOT be deregistered (img from latest 3 deploys) - %s \nImages that will NOT be deregistered (total img) - %s \n' % (images_in_use_func(), keep_images_func(), latest_images_func(), images_to_keep_func(images_in_use_func(), keep_images_func(), latest_images_func())   ))
    # print(deregister_images_func()) 

    ## for debugging
    # print('Images that will NOT be deregistered (img to keep based on past days specifield) - %s \n' % keep_images_func() )
    # print('Images that will NOT be deregistered (img from latest 3 deploys) - %s \n' % latest_images_func() )
    # print('Images that will NOT be deregistered (total img) - %s \n' % images_to_keep_func(images_in_use_func(), keep_images_func(), latest_images_func()) )

    print('[************************************************** END **************************************************]')


# for i in range(100): stars = i * '*' ; 
# print('[%s]' % (stars))

