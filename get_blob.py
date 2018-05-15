"""Fetches the git blob"""
import os
from request_handler import request_handler
from error import ResponseError


def get_blob(sha):
    """Returns the base64 content for a file
    :param fileSha: sha of the file
    """
    url = 'https://api.github.com/repos/{:1}/{:2}/git/blobs/{:3}'\
          .format(os.environ['GITHUB_USER'],
                  os.environ['GITHUB_REPO'], sha)
    headers = {'Authorization': 'token {:1}'
                                .format(os.environ['GITHUB_TOKEN']),
               'User-Agent': 'my_api'
              }
    received_request = request_handler('get', url, headers=headers)
    if received_request.status_code != 200:
        raise ResponseError(received_request.status_code,
                            received_request.json()['message'])
    else:
        return received_request.json()['content']
