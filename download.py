import boto3
import botocore

client = boto3.client('sts')

BUCKET_NAME = 'python-boto3' # replace with your bucket name
KEY = 'testfile.txt' # replace with your object key

s3 = boto3.resource('s3')

try:
    s3.Bucket(BUCKET_NAME).download_file(KEY, 'testfile.txt')
except botocore.exceptions.ClientError as e:
    if e.response['Error']['Code'] == "404":
        print("The object does not exist.")
    else:
        raise