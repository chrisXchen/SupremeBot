from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
import time


class Autofill:
    '''
    Dealing ONLY with automation on the checkout page, these methods were the fastest
    without tripping Supreme's Bot Detection. Most of the methods are self-explanatory.
    In the constructor, all I'm doing is passing a driver (which I instantiate in another class)
    and set a dictionary with the info to fill out as an instance attribute (definitely not the
    safest way, but I wasn't particularly nervous about someone hijacking my wifi).
    '''

    def __init__(self, driver):
        self.driver = driver
        self.personal_info = {
            'name': 'Christopher Chen',
            'email': 'chris@chendev.com',
            'tel': '999-999-9999',
            'address': '70 Washington Square S',
            'zip': '10012',
            'city': 'New York',
            'number': '1111334466779999',
            'month': '10',
            'year': '2024',
            'CVV': '420'
        }

    def CheckoutNow(self):
        WebDriverWait(self.driver, 20).until(
            EC.element_to_be_clickable(
                (By.XPATH, '//a[@class="button checkout"]'))
        ).click()

    '''
    I strongly believe this will be a slower version of the BoxFill method but feel free to try

    def BoxFill(self, box_type):
        WebDriverWait(self.driver, 20).until(
            EC.element_to_be_clickable(
                (By.XPATH, f'//input[@placeholder="{box_type}"]'))
        ).clear().send_keys(self.personal_info[box_type])
    '''

    def BoxFill(self, box_type):
        box_elem = self.driver.find_element_by_xpath(
            f'//input[@placeholder="{box_type}"]')
        box_elem.clear()
        box_elem.send_keys(self.personal_info[box_type])

    def ScrollFill(self, scroll_type):
        self.driver.find_element_by_xpath(
            f'//option[@value="{self.personal_info[scroll_type]}"]').click()

    def FormFillOut(self):
        '''
        This is a simple method which is just called to autofill the entire form, but I included the print
        statements so I can have accurate stats on the time it took for each autofill.
        '''

        start = time.time()

        self.BoxFill("name")
        print("name: ", str(time.time() - start))

        self.BoxFill("email")
        print("email: ", str(time.time() - start))

        self.BoxFill("tel")
        print("tel: ", str(time.time() - start))

        self.BoxFill("address")
        print("addy: ", str(time.time() - start))

        self.BoxFill("zip")
        print("zip: ", str(time.time() - start))

        self.BoxFill("number")
        print("number: ", str(time.time() - start))

        self.ScrollFill("month")
        print("scroll month: ", str(time.time() - start))

        self.ScrollFill("year")
        print("scroll year: ", str(time.time() - start))

        self.BoxFill("CVV")
        print("cvv: ", str(time.time() - start))

        # Accepting terms and conditions checkbox... smh
        checkbox_elems = self.driver.find_elements_by_xpath(
            "//ins[@class='iCheck-helper']")
        checkbox_elems[1].click()
        print("checkbox: ", str(time.time() - start))

        self.ProcessPay()

    def ProcessPay(self):
        '''
        Include this method in FormFillOut() so that it won't have to be called individually.
        '''

        self.driver.find_element_by_xpath(
            "//input[@value='process payment']").click()
