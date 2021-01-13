from bs4 import BeautifulSoup
import re

class Payload:

    '''
    There is specific data required to fulfill an add-to-cart post request.
    This data being the product's code, size code, utf-code, and CSRF Token for the
    instance you access the product.
    This code simply sets a payload attribute as an empty dictionary, and a soup
    attribute as a BeautifulSoup object, so that I can continuously use the parsed
    HTML to find and add the necessary data to my payload.

    If you don't know how BeautifulSoup works, look up their documentation.
    '''

    def __init__(self, resp):
        self.payload = {}
        self.soup = BeautifulSoup(resp.text, 'lxml')

    def FindCSRFToken(self):

        self.payload['X-CSRF-Token'] = self.soup.find(
            'meta', attrs={'name': 'csrf-token'})['content']

    def FindProductCode(self):

        self.payload['st'] = self.soup.find(
            'input', attrs={'name': 'st'})['value']

    def FindUTFCode(self):

        self.payload['utf-g'] = self.soup.find(
            'input', attrs={'name': 'utf8'})['value']

    def FindSize(self, size):
        raw_size = r'{}'.format(size)
        size_regex = re.compile(raw_size)

        for option in self.soup.find_all('option'):
            if size_regex.search(option.text):
                self.payload['s'] = option['value']
