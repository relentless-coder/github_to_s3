from parse_event import parse_event
from get_commit import get_commit
from get_blob import get_blob
from s3_client import upload_to_s3, delete_from_s3


def setup(event, context):
    commit = parse_event(event)
    files = get_commit(commit)['files']
    for f in files:
        if f.status == 'modified':
            body = get_blob(f.sha)
            upload_to_s3(body, f.filename)
        elif f.status == 'removed':
            delete_from_s3(f.filename)
