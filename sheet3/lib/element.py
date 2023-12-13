from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from lib.locators import MainPageLocators
from lib.locators import CreditCardIntroPageLocators
import logging

logging.basicConfig(level=logging.INFO, format='[%(asctime)s.%(msecs)03d] %(levelname)s %(filename)s(line:%(lineno)d): %(message)s')


class BasePageElement(object):
    def __init__(self, driver):
        self.driver = driver

    def presence_wait_until_find_element(self, element, timeout=20):
        return WebDriverWait(self.driver, timeout).until(EC.presence_of_element_located(element))

    def visibility_wait_until_find_all_elements(self, element, timeout=20):
        return WebDriverWait(self.driver, timeout).until(EC.visibility_of_all_elements_located(element))

    def presence_wait_until_find_all_elements(self, element, timeout=20):
        return WebDriverWait(self.driver, timeout).until(EC.presence_of_all_elements_located(element))

    def click_element(self, element):
        if not self.visibility_wait_until_find_all_elements(element):
            logging.error('Cannot find the element to click: {}'.format(element))
            return -1
        o = self.driver.find_element(element[0], element[1])
        logging.info('Click the element: {}'.format(element))
        o.click()








