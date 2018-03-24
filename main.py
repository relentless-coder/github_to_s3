import os
import requests


def setup():
    headers = {
            'Authoirization': 'token {:1}'.format(os.environ['github_token'])
            }
