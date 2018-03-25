from parse_event import parse_event
from get_commit import get_commit


def setup(event, context):
    commit = parse_event(event)
    files = get_commit(commit)['files']
