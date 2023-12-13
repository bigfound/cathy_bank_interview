from selenium.webdriver.common.by import By


class MainPageLocators(object):
    main_page = (By.TAG_NAME, "body")
    product_intro = (By.XPATH, '//*[@class="cubre-a-menuSortBtn -l1" and text()="產品介紹"]')

    # below locators are under product_intro
    credit_card_items = (By.XPATH, '//*[@class="cubre-a-menuSortBtn" and text()="信用卡"]/../../div[2]/a')

    # below locators are under credit_cards
    credit_cards_intro = (By.XPATH, '//*[@id="lnk_Link" and text()="卡片介紹"]')


class CreditCardIntroPageLocators(object):
    __sections = {'shopping_cards': 'section[3]',
                  'transport_cards': 'section[4]',
                  'upgraded_cube_cards': 'section[5]',
                  'terminated_cards': 'section[6]'}

    shopping_cards = (By.XPATH, '//article[@class="cubre-o-content"]/{}/div/div[2]/div/div[1]/div'.format(__sections['shopping_cards']))
    transport_cards = (By.XPATH, '//article[@class="cubre-o-content"]/{}/div/div[2]/div/div[1]/div'.format(__sections['transport_cards']))
    upgraded_cube_cards = (By.XPATH, '//article[@class="cubre-o-content"]/{}/div/div[2]/div/div[1]/div'.format(__sections['upgraded_cube_cards']))
    terminated_cards = (By.XPATH, '//article[@class="cubre-o-content"]/{}/div/div[2]/div/div[1]/div'.format(__sections['terminated_cards']))



