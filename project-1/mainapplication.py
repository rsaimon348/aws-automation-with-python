import boto3
#import sys
import click # click is used to manage command arguments

session = boto3.Session(profile_name='pythonAutomation')
# using default profile
#s3 = boto3.resource('s3')

#defining custom profile  and call using resource method of Session class
s3 = session.resource('s3')
#bucket = s3.Bucket('saimon348-test-bucket')

@click.group()
def cli():
    "script to deploys websites to aws"
    pass

#@click.command ('list-buckets')
@cli.command ('list-buckets')
def list_buckets():
    "list all s3 buckets"
    for bucket in s3.buckets.all():
        #print (type(bucket))
        print (bucket)

@cli.command ('list-bucket-objects')
# we are passing bucket name in argument instead of hard coding
@click.argument('bucket_name')
def list_bucket_objects(bucket_name):
    "List  objects in the bucket"
    for obj in s3.Bucket(bucket_name).objects.all():
        print (obj)

if  __name__ == "__main__":
    #list_buckets()
    cli()