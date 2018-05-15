import os
import base64
import boto3

S3_CLIENT = boto3.client('s3', region_name=os.environ['AWS_REGION_NAME'],
                         aws_access_key_id=os.environ['aws_access_key_id'],
                         aws_secret_access_key=os.environ['aws_secret_access_key'])


def upload_to_s3(data, key):
    """Uploads data to s3
    :param bucket: the target bucket
    :param data: base64 encoded data
    :param key: the file name
    """
    return S3_CLIENT.put_object(Bucket=os.environ['AWS_BUCKET'],
                                Key=key, Body=base64.b64decode(data).decode('utf-8'))


def delete_from_s3(key):
    """Removes a file from an s3 bucket
    :param bucket: the target bucket
    :param key: the file to be removed
    """
    return S3_CLIENT.delete_object(Bucket=os.environ['AWS_BUCKET'],
                                   Key=key)
