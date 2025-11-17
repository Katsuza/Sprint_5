import pytest
from selenium import webdriver
from locators import *
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from generators import *


@pytest.fixture
def driver():
    driver = webdriver.Chrome()
    driver.maximize_window()
    yield driver
    driver.quit()


@pytest.fixture
def exicting_user(driver):
    email = generate_email()
    password = generate_password()

    driver.get("https://stellarburgers.education-services.ru/register")
    driver.find_element(*REGISTRATION_NAME_FIELD).send_keys('Artem')
    driver.find_element(*REGISTRATION_EMAIL_FIELD).send_keys(email)
    driver.find_element(*REGISTRATION_PASSWORD_FIELD).send_keys(password)

    driver.find_element(*REGISTRATION_SUMBIT_BUTTON).click()

    WebDriverWait(driver, 5).until(EC.visibility_of_element_located(LOGIN_SUBMIT_BUTTON))

    return {"email": email, "password": password}


@pytest.fixture
def logged_user(driver, exicting_user):
    driver.get("https://stellarburgers.education-services.ru/login")

    driver.find_element(*LOGIN_EMAIL_FIELD).send_keys(exicting_user['email'])
    driver.find_element(*LOGIN_PASSWORD_FIELD).send_keys(exicting_user['password'])
    driver.find_element(*LOGIN_SUBMIT_BUTTON).click()

    WebDriverWait(driver, 5).until(EC.url_to_be("https://stellarburgers.education-services.ru/"))

    return driver