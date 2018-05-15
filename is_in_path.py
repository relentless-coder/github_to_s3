"""Checks whether as file is in path provided"""
from get_files import get_files


def is_in_path(sha):
    """Returns boolean
    Arguments:
        sha - the sha of the file
    """
    files = get_files()
    for local_file in files:
        if local_file.get('sha') == sha:
            return True
    return False
