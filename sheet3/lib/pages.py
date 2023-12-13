from selenium import webdriver
from selenium.webdriver.chrome.service import Service
from selenium.webdriver.common.by import By
from lib.locators import MainPageLocators
from lib.locators import CreditCardIntroPageLocators
from lib.element import BasePageElement
import logging
import os

logging.basicConfig(level=logging.INFO, format='[%(asctime)s.%(msecs)03d] %(levelname)s %(filename)s(line:%(lineno)d): %(message)s')


class BasePage(object):
    """Base class to initialize the base page that will be called from all pages"""

    def __init__(self, driver):
        self.driver = driver

    def open_web_page(self, url):
        self.driver.get(url)
        self.driver.set_window_size(1024, 768)
        self.driver.set_window_position(0, 0)
        # self.driver.maximize_window()


class HomePage(BasePage):
    def __init__(self, driver):
        super().__init__(driver)
        self.h = BasePageElement(self.driver)

    def open_page(self, url):
        self.open_web_page(url)

    def wait_until_home_page(self):
        return self.h.presence_wait_until_find_element(MainPageLocators.main_page)

    def save_screen_shot(self, file_path):
        return self.driver.save_screenshot(file_path)

    def click_product_intro(self):
        self.h.click_element(MainPageLocators.product_intro)

    def click_credit_cards_intro(self):
        self.h.click_element(MainPageLocators.credit_cards_intro)

    def wait_util_find_all_element(self, element):
        return self.h.visibility_wait_until_find_all_elements(element)


class CreditCardIntroPage(BasePage):
    def __init__(self, driver):
        super().__init__(driver)
        self.h = BasePageElement(self.driver)

    def get_all_credit_cards_screenshot(self, screenshot_log):
        card_category = {'shopping_cards': CreditCardIntroPageLocators.shopping_cards,
                         'transport_cards': CreditCardIntroPageLocators.transport_cards,
                         'upgraded_cube_cards': CreditCardIntroPageLocators.upgraded_cube_cards,
                         'terminated_cards': CreditCardIntroPageLocators.terminated_cards}

        total_cards = 0
        for category, element in card_category.items():
            cards = self.h.presence_wait_until_find_all_elements(element)
            logging.info('Found {} {}'.format(len(cards), category))
            total_cards += len(cards)
            for i in range(len(cards)):
                file_name = os.path.join(screenshot_log, '{}_{}.png'.format(category, i))
                logging.info('Taking screenshots, path: {}'.format(file_name))
                cards[i].screenshot(file_name)
        return total_cards

















