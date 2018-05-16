"""Based on the file status it uploads/delete to s3"""
import os
from get_blob import get_blob
from s3_client import upload_to_s3, delete_from_s3


def process_file(local_file):
    """Returns nothing
    Arguments:
        :local_file - file object
    """
    if os.environ['CONTENT_PATH']:
        temp_file = local_file['filename'].split('/')
        temp_file.pop(0)
        filename = ''.join(temp_file) if len(temp_file) == 1 else '/'.join(temp_file)
    else:
        filename = local_file['filename']
    if local_file['status'] == 'modified':
        body = get_blob(local_file['sha'])
        upload_to_s3(body, filename)
    elif local_file['status'] == 'removed':
        delete_from_s3(filename)
    elif local_file['status'] == 'renamed':
        delete_from_s3(local_file['previous_filename'])
        body = get_blob(local_file['sha'])
        upload_to_s3(body, filename)
