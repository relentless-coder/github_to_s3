"""Fetches the commit for a commit_id"""
import os
from request_handler import request_handler
from error import ResponseError


def get_commit(commit_id):
    """Returns JSON with commit data
    Arguments:
        commit_id - a valid id of the commit
    """
    url = 'https://api.github.com/repos/{:1}/{:2}/commits/{:3}'\
            .format(os.environ['GITHUB_USER'], os.environ['GITHUB_REPO'],
                    commit_id)
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
