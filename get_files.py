"""Module to fetch files from path"""
import os
from request_handler import request_handler
from error import ResponseError


def get_files():
    """Returns JSON if success, else raises error"""
    files = []
    if files:
        return files
    url = 'https://api.github.com/repos/{:1}/{:2}/contents/{:3}'\
          .format(os.environ['GITHUB_USER'], os.environ['GITHUB_REPO'],
                  os.environ['CONTENT_PATH'])
    headers = {'Authorization': 'token {:1}'
                                .format(os.environ['GITHUB_TOKEN']),
               'User-Agent': 'my_api'
              }
    received_request = request_handler('get', url, headers=headers)
    if received_request.status_code != 200:
        raise ResponseError(received_request.status_code,
                            received_request.json()['message'])
    else:
        return received_request.json()
