"""Based on the file status it uploads/delete to s3"""
import os
from get_blob import get_blob
from s3_client import upload_to_s3, delete_from_s3


def getFilename(file_object):
    """Returns filename extracted from the file object
    Arguments:
        file_object - a github fileobject with file details
    """
    
    if os.environ['CONTENT_PATH']:
        temp_dir = os.environ['CONTENT_PATH'].split('/')
        max_index = 0
        for dr in temp_dir:
            max_index = max(max_index, file_object['filename'].index(dr))

        return file_object['filename'][max_index:]
    else:
        return  file_object['filename']


def process_file(local_file):
    """Returns boolean
    Arguments:
        :local_file - file object
    """
    if os.environ['CONTENT_PATH']:
        if not is_in_path(local_file.get('sha')):
            return False
    
    filename = getFilename(local_file)
    
    file_status = local_file['status']
    
    if file_status == 'modified':
        body = get_blob(local_file['sha'])
        upload_to_s3(body, filename)
    elif file_status == 'removed':
        delete_from_s3(filename)
    elif file_status == 'renamed':
        delete_from_s3(local_file['previous_filename'])
        body = get_blob(local_file['sha'])
        upload_to_s3(body, filename)
    else:
        return False

    return True
