import os
import json
from request_handler import request_handler
from error import ResponseError


def get_commit(commitId):
    url = 'https://api.github.com/repos/{:1}/{:2}/commits/{:3}'\
            .format(os.environ('OWNER'), os.environ('REPO'), commitId)
    headers = {'Authorization': 'token {:1}'
               .format(os.environ('GITHUB_TOKEN'))}
    r = request_handler('get', url, headers=headers)
    if r.status_code != 200:
        raise ResponseError(r.status_code, r.json().message)
    else:
        return json.loads(r.json())
