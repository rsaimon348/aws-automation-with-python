import boto3
#import sys
import click # click is used to manage command arguments
from botocore.exceptions import ClientError

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

@cli.command ('create-bucket')
@click.argument ('bucket_name')
def create_bucket(bucket_name):
        "Create bucket as provided name"
        #print (session.region_name)
        new_bucket = None
        try:
                new_bucket = s3.create_bucket(Bucket = bucket_name)
        except  ClientError  as e:
                if e.response ['Error']['Code'] == "BucketAlreadyOwnedByYou" :
                        new_bucket = s3.Bucket(bucket_name)
                else:
                        raise e

        policy = """
                {
                        "Version": "2012-10-17",
                        "Statement": [
                        {
                                "Sid": "PublicReadGetObject",
                                "Effect": "Allow",
                                "Principal": "*",
                                "Action": ["s3:GetObject"],
                                "Resource": ["arn:aws:s3:::%s/*"]
                        }
                        ]
                }
        """ % new_bucket.name
        # defining the policy for the bucket to host static website
        policy = policy.strip()
        pol = new_bucket.Policy()
        pol.put(Policy=policy)

        #s3.Bucket(new_bucket.name).upload_file('index.html','index.html')

        #bucket = s3.Bucket(new_bucket.name)
        ws  = new_bucket.Website()
        ws.put(WebsiteConfiguration={'ErrorDocument': {'Key': 'error.html'},'IndexDocument': {'Suffix': 'index.html'}})

        s3.Bucket(new_bucket.name).upload_file('index.html','index.html',ExtraArgs={'ContentType':'text/html'})

        return
        

if  __name__ == "__main__":
    #list_buckets()
    cli()