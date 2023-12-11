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
        global driver, log_folder
        chrome_driver_path = './chromedriver.exe'
        service = Service(chrome_driver_path)
        driver = webdriver.Chrome(service=service)
        driver.set_window_size(1024, 768)
        driver.set_window_position(0, 0)

        log_folder = os.path.join(os.path.dirname(__file__), "log")
        create_log_folder(log_folder)
        yield
        driver.quit()
        copy_to_log_folder = [log_filename, step1_screenshot, case2_screenshot]
        for file in copy_to_log_folder:
            if not os.path.isfile(file):
                pytest.error('Copy the {} to the log folder failed.'.format(file))
            shutil.copyfile(file, os.path.join(log_folder, file))

    @allure.title("Test case1: Taking screen in home page")
    @allure.severity(allure.severity_level.CRITICAL)
    def test_home_page_take_screenshot(self):
        global step1_screenshot
        step1_screenshot = 'Test_case1_home_page_screenshot.png'
        logger.info('Go to CathayBank home page and take a screenshot.')
        logger.info('Opening the CathayBank home page')
        logger.info('https://www.cathaybk.com.tw/cathaybk/')
        driver.get("https://www.cathaybk.com.tw/cathaybk/")
        WebDriverWait(driver, 10).until(EC.presence_of_element_located((By.TAG_NAME, "body")))
        logger.info('Taking a screenshot, file name: {}'.format(step1_screenshot))
        result = driver.save_screenshot(step1_screenshot)
        if not result:
            pytest.fail('Screenshot failed')
        logger.info('Completed screenshot')

    @allure.title("Test case2: Calculating items in credit card list")
    @allure.severity(allure.severity_level.NORMAL)
    def test_calculate_items_in_credit_card_list(self):
        global case2_screenshot
        case2_screenshot = 'Test_case2_items_in_credit_card_list.png'
        logger.info('Confirm how many items in the credit card list')
        products_intro = driver.find_element(By.XPATH, '//*[@class="cubre-a-menuSortBtn -l1" and text()="產品介紹"]')
        logger.info('Click the products introduction tab')
        products_intro.click()
        credit_cards = WebDriverWait(driver, 10).until(EC.visibility_of_all_elements_located((By.XPATH, '//*[@class="cubre-a-menuSortBtn" and text()="信用卡"]/../../div[2]/a')))
        logger.info('Taking a screenshot, file name: {}'.format(case2_screenshot))
        result = driver.save_screenshot(case2_screenshot)
        if not result:
            pytest.fail('Screenshot failed')
        logger.info('Found {} items in the credit card list'.format(len(credit_cards)))
        assert len(credit_cards) == 8, 'Expect to find 8 items'

    @allure.title("Test case3: Confirm how many credit cards and taking screenshot for cards")
    @allure.severity(allure.severity_level.BLOCKER)
    def test_calculate_credit_cards_num(self):
        screenshot_log = os.path.join(log_folder, 'credit_cards_nums')
        create_log_folder(screenshot_log)
        logger.info('Confirm how many credit cards and taking screenshot for cards')
        credit_cards_intro = driver.find_element(By.XPATH, '//*[@id="lnk_Link" and text()="卡片介紹"]')
        credit_cards_intro.click()
        check_list = {'shopping_cards':      'section[3]',
                      'transport_cards':     'section[4]',
                      'upgraded_cube_cards': 'section[5]',
                      'terminated_cards':    'section[6]'}

        total_cards = 0
        for card_category, section in check_list.items():
            cards = WebDriverWait(driver, 20).until(EC.presence_of_all_elements_located((By.XPATH, '//article[@class="cubre-o-content"]/{}/div/div[2]/div/div[1]/div'.format(section))))
            logger.info('Found {} {}'.format(len(cards), card_category))
            total_cards += len(cards)
            for i in range(len(cards)):
                file_name = os.path.join(screenshot_log, '{}_{}.png'.format(card_category, i))
                logger.info('Taking screenshots, path: {}'.format(file_name))
                cards[i].screenshot(file_name)

        if len(os.listdir(screenshot_log)) != total_cards:
            pytest.fail('The quantity of screenshot files is not match the quantity of total cards')













