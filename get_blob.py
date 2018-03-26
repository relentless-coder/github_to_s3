import os
import json
from request_handler import request_handler
from error import ResponseError


def get_blob(fileSha):
    """Returns the base64 content for a file
    :param fileSha: sha of the file
    """
    url = 'https://api.github.com/repos/{:1}/{:2}/git/blobs/{:3}'\
          .format(os.environ('GITHUB_USER'),
                  os.environ('GITHUB_REPO'), fileSha)
    headers = {'Authorization': 'token {:1}'
               .format(os.environ('GITHUB_TOKEN'))}
    r = request_handler('get', url, headers=headers)
    if r.status_code != 200:
        raise ResponseError(r.status_code,
                            json.loads(r.json())['message'])
    else:
        return json.loads(r.json())['content']
