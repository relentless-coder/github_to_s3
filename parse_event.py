import json
import os


def parse_event(event):
    attrs = event.Records[0].Sns.MessageAttributes
    try:
        if attrs.get('X-Github-Event') and attrs.get('X-Github-Event') == 'push':
            eventObj = json.loads(event.Records[0].Sns.Message)
            foundBranch = eventObj.ref.split('/')[-1]
            if foundBranch == os.environ('branch'):
                return eventObj['head_commit']['id']
            else:
                return False
    except AttributeError:
        raise
