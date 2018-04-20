import os
from parse_event import parse_event
from get_commit import get_commit
from is_in_path import is_in_path
from process_file import process_file


def setup(event, context):
    commit = parse_event(event)
    files = get_commit(commit)['files']
    for f in files:
        if os.environ('CONTENT_PATH'):
            if is_in_path(f.get('sha')):
                process_file(f)
        else:
            process_file(f)
