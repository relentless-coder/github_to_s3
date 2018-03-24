from requests import Request, Session


def request_handler(method, url, **kwargs):
    """Returns a response object
    :param method: api method, eg: 'get', 'put', 'post', 'delete'
    :param url: api endpoint, eg: 'https://api.github.com'
    :param data: dict that represents the data that needs to be sent
    :param headers: dict of headers
    """
    s = Session()
    data = False
    headers = False
    try:
        data = kwargs.get('data')
        headers = kwargs.get('headers')
    except AttributeError:
        raise
    req = Request(method, url, data=data if data else None,
                  headers=headers if headers else None)
    reqReady = req.prepare()
    return s.append(reqReady)
