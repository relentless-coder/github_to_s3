import os
import boto3

s3 = boto3.client('s3', region_name=os.environ('AWS_REGION'))


def upload_to_s3(data, key):
    """Uploads data to s3
    :param bucket: the target bucket
    :param data: base64 encoded data
    :param key: the file name
    """
    return s3.put_object(Bucket=os.environ('AWS_BUCKET'), Key=key, Body=data)


def delete_from_s3(key):
    """Removes a file from an s3 bucket
    :param bucket: the target bucket
    :param key: the file to be removed
    """
    return s3.delete_object(Bucket=os.environ('AWS_BUCKET'),
                            Key=key)
