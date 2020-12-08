import pytest
from selenium.webdriver.chrome.webdriver import WebDriver
from selenium.webdriver.common.keys import Keys
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from selenium.webdriver import ActionChains
from locators import Locator as Locator
from common import *


def test_log_in(driver: WebDriver):
    """
    Given User is on sign in page
    When User fills the login and password box and clicks on button "Zaloguj się"
    Then He is logged in.
    """
    login_button = wait_element_clickable_and_click(
        driver, Locator.LOG_IN_BUTTON)
    login_entry_box = wait_element_visible(driver, Locator.LOGIN_BOX_ENTRY, 7)
    login_entry_box.send_keys(Locator.USER_NAME)
    pin_box = wait_element_visible(driver, Locator.PIN_BOX_ENTRY)
    pin_box.send_keys(Locator.PASSWORD)
    login_entry_box.send_keys(Keys.ENTER)
    wait_element_clickable(driver, Locator.VAR_CHECK_AFTER_LOGIN)

def test_log_in_empty_boxes(driver: WebDriver):
    """
    Given User is on sign in page
    When User don't fills the login and password box and clicks on button "Zaloguj się"
    Then He is not logged in.
    """
    login_button = wait_element_clickable_and_click(
        driver, Locator.LOG_IN_BUTTON)
    login_entry_box = wait_element_visible(driver, Locator.LOGIN_BOX_ENTRY, 7)
    login_entry_box.send_keys(Locator.USER_NAME_EMPTY)
    pin_box = wait_element_visible(driver, Locator.PIN_BOX_ENTRY)
    pin_box.send_keys(Locator.PASSWORD_EMPTY)
    login_entry_box.send_keys(Keys.ENTER)
    wait_element_visible(driver, Locator.VAR_CHECK_AFTER_LOGIN_EMPTY)


def test_log_in_wrong_password(driver: WebDriver):
    """
    Given User is on sign in page
    When User fills the correct login but wrong password and clicks on button "Zaloguj się"
    Then He is not logged in.
    """
    login_button = wait_element_clickable_and_click(
        driver, Locator.LOG_IN_BUTTON)
    login_entry_box = wait_element_visible(driver, Locator.LOGIN_BOX_ENTRY, 7)
    login_entry_box.send_keys(Locator.USER_NAME)
    pin_box = wait_element_visible(driver, Locator.PIN_BOX_ENTRY)
    pin_box.send_keys(Locator.PASSWORD_EMPTY)
    login_entry_box.send_keys(Keys.ENTER)
    wait_element_visible(driver, Locator.VAR_CHECK_AFTER_LOGIN_EMPTY)

def test_log_in_wrong_login(driver: WebDriver):
    """
    Given User is on sign in page
    When User entrys wrong login but correct password and clicks on button "Zaloguj się"
    Then He is not logged in.
    """
    login_button = wait_element_clickable_and_click(
        driver, Locator.LOG_IN_BUTTON)
    login_entry_box = wait_element_visible(driver, Locator.LOGIN_BOX_ENTRY, 7)
    login_entry_box.send_keys(Locator.USER_NAME_EMPTY)
    pin_box = wait_element_visible(driver, Locator.PIN_BOX_ENTRY)
    pin_box.send_keys(Locator.PASSWORD)
    login_entry_box.send_keys(Keys.ENTER)
    wait_element_visible(driver, Locator.VAR_CHECK_AFTER_LOGIN_EMPTY)


def test_hover_navbar(driver: WebDriver):
    """
    Given User is on main page
    When User moves the cursor over the category
    Then Hover navbar is visible and subcategory is clickable
    """
    nav_categories = {Locator.MEN_BUTTON: Locator.NAV_CATEGORY_BUTTON,
                      Locator.WOMEN_BUTTON: Locator. NAV_CAT_BUTTON_WOMEN,
                      Locator.KIDS_BUTTON: Locator. NAV_CAT_BUTTOM_KIDS}
    for key, value in nav_categories.items():
        move_to_element(driver, key)
        wait_element_clickable(driver, value)


def test_corect_link_navbar(driver: WebDriver):
    """
    Given User is on main page
    When User moves the cursor over the category and click on the subcategory
    Then He is redirected to correct page
    """
    nav_categories = {Locator.MEN_BUTTON: [Locator.NAV_CATEGORY_BUTTON, Locator.TEXT_MEN_CATEGORY],
                      Locator.WOMEN_BUTTON: [Locator. NAV_CAT_BUTTON_WOMEN, Locator.TEXT_WOMEN_SUBCATEGORY],
                      Locator.KIDS_BUTTON: [Locator.NAV_CAT_BUTTOM_KIDS, Locator.TEXT_KIDS_SUBCATEGORY]}
    for key, value in nav_categories.items():
        move_to_element(driver, key)
        wait_element_clickable_and_click(driver, value[0])
        wait_element_presence(driver, value[1])
        driver.back()


def test_sorting_by_price_ascen(driver: WebDriver):
    """
    Given User is on men page
    When User chooses to sort by increasing prices
    Then List of items is sorted by increasing prices
    """
    move_to_element(driver, Locator.MEN_BUTTON)
    wait_element_clickable_and_click(driver, Locator.NAV_CATEGORY_BUTTON)
    wait_element_clickable_and_click(driver, Locator.SORTING_BOX)
    wait_element_clickable_and_click(driver, Locator.SORT_BY_PRICE_ASCEN)
    prices = driver.find_elements_by_class_name("price")
    del prices[48:]
    prices_list = []
    for price in prices:
        price_with_zl = price.text.replace(" zł", "")
        prices_list.append(price_with_zl)
    assert sorted(prices_list) == prices_list


def test_sorting_by_price_descent(driver: WebDriver):
    """
    Given User is on women page subcategory "Baleriniki"
    When The user chooses to sort by decreasing prices
    Then List of items is sorted by decreasing prices
    """
    move_to_element(driver, Locator.WOMEN_BUTTON)
    wait_element_clickable_and_click(driver, Locator.NAV_CAT_BUTTON_WOMEN)
    wait_element_clickable_and_click(driver, Locator.SORTING_BOX)
    wait_element_clickable_and_click(driver, Locator.SORT_BY_PRICE_DESCEN)
    prices = driver.find_elements_by_class_name("price")
    del prices[48:]
    prices_list = []
    for price in prices:
        price_with_zl = price.text.replace(" zł", "")
        prices_list.append(price_with_zl)
    assert sorted(prices_list, reverse=True) == prices_list


def test_sorting_by_name_ascent(driver: WebDriver):
    """
    Given
    When
    Then
    """
    move_to_element(driver, Locator.WOMEN_BUTTON)
    wait_element_clickable_and_click(driver, Locator.NAV_CAT_BUTTON_WOMEN)
    wait_element_clickable_and_click(driver, Locator.SORTING_BOX)
    wait_element_clickable_and_click(driver, Locator.SORT_BY_NAME_ASCEN)
    driver.implicitly_wait(5)
    elements_names = driver.find_elements_by_class_name("product-name")
    products_names_list = []
    for product in elements_names:
        products_names_list.append(product.text)
    del products_names_list[48:]
    assert sorted(products_names_list) == products_names_list


def test_sorting_by_name_descent(driver: WebDriver):
    """
    Given
    When
    Then
    """
    move_to_element(driver, Locator.WOMEN_BUTTON)
    wait_element_clickable_and_click(driver, Locator.NAV_CAT_BUTTON_WOMEN)
    wait_element_clickable_and_click(driver, Locator.SORTING_BOX)
    wait_element_clickable_and_click(driver, Locator.SORT_BY_NAME_DESCEN)
    driver.implicitly_wait(5)
    elements_names = driver.find_elements_by_class_name("product-name")
    products_names_list = []
    for product in elements_names:
        products_names_list.append(product.text)
    del products_names_list[48:]
    assert sorted(products_names_list, reverse=True) == products_names_list
