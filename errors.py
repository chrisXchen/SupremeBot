
class PostRequestError(Exception):
    '''
    I'm creating my own error so that in case I need more functionality in the future, I
    would be able to raise errors when I could predict something will go wrong.
    '''

    def __init__(self, resp):
        self.resp = resp
        super().__init__(
            f'Unable to send Post Request. Status Code: {self.resp.status_code}')
