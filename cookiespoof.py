import requests
import time

from locator import locate
from errors import PostRequestError


class CookieSpoof:

    '''
    I instantiate the category and name so it could be used in the locate function I import from the locator module.
    I also DON'T instantiate the webdriver or requests Session here because I'd rather just pass the entire webdriver
    or session object as an argument which I can write behaviors for.
    '''

    headers = {
        'User-Agent': 'Mozilla/5.0 (Macintosh; Intel Mac OS X 11_1_0) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/87.0.4280.88 Safari/537.36'}

    def __init__(self, driver, session, category, name):
        self.category = category
        self.name = name
        self.driver = driver
        self.sess = session
        if locate(self.category, self.name):
            self.start = time.time()
            self.url_suffix = locate(self.category, self.name)

    def FindProduct(self):
        '''
        This was meant to be an improved version of the 'if locate(self.category, self.name):' in the constructor
        because I would rather call a method to create that attribute (self.url_suffix) so as to explicitly force
        the program to halt execution until this method was finished. But I believe instantiating it will have the
        same effect.
        '''
        pass

    def GenBaseCookie(self):
        '''
        Generates the 'nearly' empty cookie from the driver
        '''
        base_cookie = self.driver.get_cookies()
        return base_cookie

    def PassBaseCookie(self, first_cookie):
        '''
        Passes that nearly empty cookie to the Requests.Session()
        '''
        passed_cookie = [self.sess.cookies.set(
            c['name'], c['value']) for c in first_cookie]

        return passed_cookie

    def GenResponse(self):
        '''
        Uses self.url_suffix to directly access the product page and returns the get response, so that I can
        reference it in the Payload.
        '''
        resp = self.sess.get(
            f'https://www.supremenewyork.com{self.url_suffix}', headers=self.headers)

        return resp

    def GenATCCookie(self, payload, key):
        '''
        Here I am using the data I got with the Payload class to send a post request that'll generate my add-to-
        cart cookie. To do this, I need to push the post request with the payload AND user-agent (this is just one
        small part of the necessities that go into bypassing Google's ReCAPTCHA).

        I use a conditional to ensure that my post request was successful, otherwise I raise my own custom error because
        the program will crash unless this ATCCookie is generated.
        '''
        resp = self.sess.post(
            f'https://www.supremenewyork.com/shop/{payload.get(key)}/add', data=payload, headers=self.headers)

        if resp.status_code == requests.codes.ok:
            atc_cookie = resp.cookies.get_dict()
            return atc_cookie

        else:
            print(
                "Something went wrong in: GenATCCookie(self, payload, product_code_key")
            print(
                "You likely don\'t have the correct cookie, so continuing the program would result in failure.")
            raise PostRequestError(resp)

    def PassATCCookie(self, atc_cookie):
        '''
        Here I'm just passing the ATCCookie from the Requests.Session() to the driver that's been untouched on the
        view/edit cart page
        '''
        passed_cookie = [{'name': name, 'value': value}
                         for name, value in atc_cookie.items()]
        c = [self.driver.add_cookie(c) for c in passed_cookie]

        return c
