from get_files import get_files


def is_in_path(sha):
    files = get_files()
    for f in files:
        if f.get('sha') == sha:
            return True
    return False
