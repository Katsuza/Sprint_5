import pytest
from selenium import webdriver
from locators import *
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC


@pytest.fixture
def driver():
    driver = webdriver.Chrome()
    driver.maximize_window()
    yield driver
    driver.quit()


@pytest.fixture
def exicting_user():
    user = {'email': 'Katsu123@ya.ru', 'password': 'Katsu123@ya.ru'}
    return user


@pytest.fixture
def logged_user(driver, exicting_user):
    driver.get("https://stellarburgers.education-services.ru/login")

    driver.find_element(*LOGIN_EMAIL_FIELD).send_keys(exicting_user['email'])
    driver.find_element(*LOGIN_PASSWORD_FIELD).send_keys(exicting_user['password'])
    driver.find_element(*LOGIN_SUBMIT_BUTTON).click()

    WebDriverWait(driver, 5).until(EC.url_to_be("https://stellarburgers.education-services.ru/"))

    return driver