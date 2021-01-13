from cookiespoof import CookieSpoof
from payload import Payload
from autofill import Autofill
from selenium import webdriver
from selenium.common.exceptions import NoSuchElementException
import requests
import time


class Buy:
    '''
    I made the Buy class to contain all the other classes I wrote. This way, everything revolves around this class.
    This class instantiates all the necessary drivers and sessions then passes them as parameters when
    instantiating the other objects. I designed this program so that this Buy class uses a 'has-a' relationship with
    Autofill, Payload, and CookieSpoof classes.
    '''

    def __init__(self, driver_path, category, name):
        self.category = category
        self.name = name
        '''
        In case you want to make the browser headless, insert this code ABOVE self.driver and add, options=self.options
        as a parameter to webdriver.Chrome(...)
        ----
        self.options = webdriver.ChromeOptions()
        self.options.add_argument('headless')
        ----
        '''
        self.driver = webdriver.Chrome(
            executable_path=driver_path)
        self.sess = requests.Session()

        self.Cookie = CookieSpoof(
            driver=self.driver, session=self.sess, category=self.category, name=self.name)
        self.Payload = Payload(self.Cookie.GenResponse())
        self.Autofill = Autofill(driver=self.driver)

    def Purchase(self, url, size):
        '''
        The one method to call on the Buy object you instantiate so that the entire program will run.
        '''
        self.ConstructBase(url)
        print('Construct Base: ', str(time.time() - self.Cookie.start))

        self.BuildPayload('Medium')
        print('Build Payload: ', str(time.time() - self.Cookie.start))

        self.CookieSpoof()
        print('Spoof Cookies + Refresh: ', str(time.time() - self.Cookie.start))

        '''
        These two methods (.CookieSpoof() and .CheckoutNow()) BY FAR take the longest, for reasons
        explained in the README
        '''

        self.Autofill.CheckoutNow()
        print('Driver to Checkout Page: ', str(
            time.time() - self.Cookie.start))

        self.StartAutoFill()
        print('Autofill: ', str(time.time() - self.Cookie.start))

    def ConstructBase(self, url):
        '''
        I am running a get method on the driver to get me to the view/edit cart page, then
        using that url to generate and pass the base cookie from the driver to the session.
        '''
        self.driver.get(url)
        self.Cookie.PassBaseCookie(self.Cookie.GenBaseCookie())

    def BuildPayload(self, size):
        '''
        I'm building the payload, quite self-explanatory. Refer to the payload class if you're confused.
        '''
        self.Payload.FindCSRFToken()
        self.Payload.FindProductCode()
        self.Payload.FindSize(size)
        self.Payload.FindUTFCode()

    def CookieSpoof(self):
        '''
        I'm generating and passing the ATCCookie, but I also included a driver refresh because, in my tests,
        I found it to enable direct click from view/edit cart page to the Checkout Page, AFTER the cookie has been added,
        however it also makes it slower. I suggest you test it on your system and decide on whether to use it.
        '''
        self.Cookie.PassATCCookie(
            self.Cookie.GenATCCookie(self.Payload.payload, 'st'))
        #self.driver.refresh()

    def StartAutoFill(self):
        '''
        I start the autofill, but if the name attribute isn't there, that likely means I'm not on the right page,
        so I avoid using conditionals and handle the error so that the bot clicks on the Checkout Now button (if it's
        on the page) then starts the autofill.
        '''
        try:
            self.Autofill.FormFillOut()
        except NoSuchElementException:
            self.Autofill.CheckoutNow()
            time.sleep(.350)
            self.Autofill.FormFillOut()
