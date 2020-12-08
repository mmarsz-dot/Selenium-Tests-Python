import os
from selenium.webdriver.common.by import By

class Locator:
    USER_NAME = os.environ.get('TEST_USER')
    PASSWORD = os.environ.get('TEST_PASSWORD')
    USER_NAME_EMPTY = ""
    PASSWORD_EMPTY = ""
    VAR_CHECK_AFTER_LOGIN_EMPTY = (By.XPATH, "//h3[contains(text(),'Podany login lub hasło nie jest poprawne.')]")
    LOG_IN_BUTTON = (By.CSS_SELECTOR,"header.site-header:nth-child(1) div.site-menu div.container div.user-menu-wrapper ul:nth-child(1) li:nth-child(1) a:nth-child(1) div.item-body > strong:nth-child(1)")
    LOGIN_BOX_ENTRY = (By.ID, "signin_login_input")
    PIN_BOX_ENTRY = (By.ID, "signin_pass_input")
    VAR_CHECK_AFTER_LOGIN = (By.CSS_SELECTOR, "header.site-header:nth-child(1) div.site-menu div.container div.user-menu-wrapper ul:nth-child(1) li:nth-child(1) a:nth-child(1) div.item-body > strong:nth-child(1)")
    MEN_BUTTON = (By.XPATH, "//a[contains(text(),'Mężczyźni')]")
    NAV_CATEGORY_BUTTON = (By.XPATH, "//header/div[3]/div[1]/div[1]/div[1]/div[1]/div[1]/ul[2]/li[1]/ul[1]/li[1]/ul[1]/li[1]/a[1]")
    WOMEN_BUTTON = (By.XPATH, "//a[contains(text(),'Kobiety')]")
    NAV_CAT_BUTTON_WOMEN = (By.XPATH, "//a[contains(text(),'Balerinki')]")
    KIDS_BUTTON = (By.XPATH, "//a[contains(text(),'Dzieci')]")
    NAV_CAT_BUTTOM_KIDS = ((By.XPATH, "//header/div[3]/div[1]/div[1]/div[1]/div[1]/div[1]/ul[2]/li[3]/ul[1]/li[1]/ul[1]/li[1]/a[1]"))
    TEXT_MEN_CATEGORY = (By.XPATH, "//h1[contains(text(),'Męskie buty do biegania')]")
    TEXT_WOMEN_SUBCATEGORY = (By.XPATH, "//h1[contains(text(),'Balerinki')]")
    TEXT_KIDS_SUBCATEGORY = (By.XPATH, "//h1[contains(text(),'Buty dziecięce do biegania')]")

    SORTING_BOX = (By.XPATH, "//span[contains(text(),'po nazwie rosnąco')]")
    SORT_BY_PRICE_ASCEN = (By.LINK_TEXT, "po cenie rosnąco")
    SORT_BY_PRICE_DESCEN = (By.LINK_TEXT, "po cenie malejąco")
    SORT_BY_NAME_ASCEN = (By.LINK_TEXT, "po nazwie rosnąco")
    SORT_BY_NAME_DESCEN = (By.LINK_TEXT, "po nazwie malejąco")