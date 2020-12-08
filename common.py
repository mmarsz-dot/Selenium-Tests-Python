import pytest
from selenium import webdriver
from selenium.webdriver.chrome.webdriver import WebDriver
from selenium.webdriver.common.keys import Keys
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from locators import Locator as Locator
from selenium.webdriver import ActionChains


PATH = "D:\chromedriver.exe"
@pytest.fixture
def driver() -> WebDriver:
    driver = webdriver.Chrome(PATH)
    driver.implicitly_wait(10)
    driver.get("https://marionex.pl/")
    yield driver
    driver.quit()


def wait_element_presence(driver, locator, time=13):
    element = WebDriverWait(driver, time).until(EC.presence_of_element_located(locator))
    return element

def wait_element_visible(driver, locator, time=13):
    element = WebDriverWait(driver, time).until(EC.visibility_of_element_located(locator))
    return element

def wait_element_clickable(driver, locator, time=13):
    element = WebDriverWait(driver, time).until(EC.element_to_be_clickable(locator))
    return element

def wait_element_clickable_and_click(driver, locator, time=13):
    element = WebDriverWait(driver, time).until(EC.element_to_be_clickable(locator)).click()
    return element

def move_to_element(driver, locator, time=10):
    action_chain = ActionChains(driver)
    element = WebDriverWait(driver, time).until(EC.element_to_be_clickable(locator))
    action_chain.move_to_element(element).perform()
