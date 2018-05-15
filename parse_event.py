"""Parses event"""
import json
import os


def parse_event(event):
    """Return the head commit id
    Arguments:
    :event - the event object that contains the commit info
    """
    attrs = event.get('Records')[0].get('Sns').get('MessageAttributes')

    try:
        if attrs.get('X-Github-Event') and attrs.get('X-Github-Event').get('Value') == 'push':
            event_obj = json.loads(event.get('Records')[0].get('Sns').get('Message'))
            found_branch = event_obj['ref'].split('/')[-1]
            if found_branch == os.environ['branch']:
                return event_obj['head_commit']['id']
            return False
        return False
    except AttributeError:
        raise
