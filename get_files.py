import os
import json
from request_handler import request_handler
from error import ResponseError


def get_files():
    files = []
    if files:
        return files
    url = 'https://api.github.com/repos/{:1}/{:2}/contents/{:3}'\
          .format(os.environ('GITHUB_USER'), os.environ('GITHUB_REPO'),
                  os.environ('CONTENT_PATH'))
    headers = {'Authorization': 'token {:1}'
               .format(os.environ('GITHUB_TOKEN'))}
    r = request_handler('get', url, headers=headers)
    if r.status_code != 200:
        raise ResponseError(r.status_code, json.loads(r.json()['message']))
    else:
        files = json.loads(r.json())
        return files
