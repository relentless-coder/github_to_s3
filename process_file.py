from get_blob import get_blob
from s3_client import upload_to_s3, delete_from_s3


def process_file(f):
    if f.status == 'modified':
        body = get_blob(f.sha)
        upload_to_s3(body, f.filename)
    elif f.status == 'removed':
        delete_from_s3(f.filename)
    elif f.status == 'renamed':
        delete_from_s3(f.previous_filename)
        body = get_blob(f.sha)
        upload_to_s3(body, f.filename)
