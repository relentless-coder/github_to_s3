"""
Entry module that the lambda handler would call

"""
import os

from parse_event import parse_event
from get_commit import get_commit
from is_in_path import is_in_path
from process_file import process_file


def setup(event, context):
    """Read event and call process_file accordingly
    Arguments
    :event, event object passed by lambda

    """
    commit = parse_event(event)
    if commit != False:
        files = get_commit(commit)['files']
        for local_file in files:
                process_file(local_file)
