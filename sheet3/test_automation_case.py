import pytest
import logging
import datetime
import os
import shutil
import allure
from selenium import webdriver
from selenium.webdriver.chrome.service import Service
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from lib.util import create_log_folder
from lib.locators import MainPageLocators
from lib.locators import CreditCardIntroPageLocators
from lib.pages import BasePage
from lib.pages import HomePage
from lib.pages import CreditCardIntroPage
from lib.element import BasePageElement
from lib.locators import MainPageLocators

logger = logging.getLogger()
logger.setLevel(logging.INFO)
formatter = logging.Formatter('[%(asctime)s.%(msecs)03d] %(levelname)s %(filename)s(line:%(lineno)d): %(message)s',
                              datefmt='%Y%m%d %H:%M:%S')
log_filename = datetime.datetime.now().strftime("%Y-%m-%d_%H_%M_%S_console.log")
fh = logging.FileHandler(log_filename)
fh.setLevel(logging.DEBUG)
fh.setFormatter(formatter)
logger.addHandler(fh)


class TestCases:
    @pytest.fixture(scope='class', autouse=True)
    def setup_teardown(self):
        global driver, log_folder, chrome_driver_path
        chrome_driver_path = './chromedriver.exe'
        log_folder = os.path.join(os.path.dirname(__file__), "log")
        create_log_folder(log_folder)
        service = Service(chrome_driver_path)
        driver = webdriver.Chrome(service=service)
        yield
        copy_to_log_folder = [log_filename, step1_screenshot, case2_screenshot]
        for file in copy_to_log_folder:
            if not os.path.isfile(file):
                pytest.error('Copy the {} to the log folder failed.'.format(file))
            shutil.copyfile(file, os.path.join(log_folder, file))

    @allure.title("Test case1: Taking screen in home page")
    @allure.severity(allure.severity_level.CRITICAL)
    def test_home_page_take_screenshot(self):
        global step1_screenshot, homepage
        step1_screenshot = 'Test_case1_home_page_screenshot.png'
        h_url = 'https://www.cathaybk.com.tw/cathaybk/'
        logger.info('Go to CathayBank home page and take a screenshot.')
        logger.info('Opening the CathayBank home page')
        logger.info(h_url)
        homepage = HomePage(driver)
        homepage.open_page(h_url)
        if not homepage.wait_until_home_page():
            logger.error('Opened home page failed.')
        logger.info('Taking a screenshot, file name: {}'.format(step1_screenshot))
        result = homepage.save_screen_shot(step1_screenshot)
        if not result:
            pytest.fail('Screenshot failed')
        logger.info('Completed screenshot')

    @allure.title("Test case2: Calculating items in credit card list")
    @allure.severity(allure.severity_level.NORMAL)
    def test_calculate_items_in_credit_card_list(self):
        global case2_screenshot
        case2_screenshot = 'Test_case2_items_in_credit_card_list.png'
        logger.info('Confirm how many items in the credit card list')
        homepage.click_product_intro()
        items_under_credit_cards = homepage.wait_util_find_all_element(MainPageLocators.credit_card_items)
        logger.info('Taking a screenshot, file name: {}'.format(case2_screenshot))
        result = homepage.save_screen_shot(case2_screenshot)
        if not result:
            pytest.fail('Screenshot failed')
        logger.info('Found {} items in the credit card list'.format(len(items_under_credit_cards)))
        assert len(items_under_credit_cards) == 8, 'Expect to find 8 items'

    @allure.title("Test case3: Confirm how many credit cards and taking screenshot for cards")
    @allure.severity(allure.severity_level.BLOCKER)
    def test_calculate_credit_cards_num(self):
        screenshot_log = os.path.join(log_folder, 'credit_cards_nums')
        create_log_folder(screenshot_log)
        logger.info('Confirm how many credit cards and taking screenshot for cards')
        homepage.click_credit_cards_intro()
        credit_intro_page = CreditCardIntroPage(driver)
        total_cards = credit_intro_page.get_all_credit_cards_screenshot(screenshot_log)
        if len(os.listdir(screenshot_log)) != total_cards:
            pytest.fail('The quantity of screenshot files is not match the quantity of total cards')













