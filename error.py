class Error(Exception):
    pass


class ResponseError(Error):
    def __init__(self, status, message):
        self.status = status
        self.message = message
