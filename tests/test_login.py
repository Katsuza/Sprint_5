import pytest
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from locators import *


def test_login_from_main_page_log_in_to_account_button(driver, exicting_user):
    driver.get("https://stellarburgers.education-services.ru/")
    driver.find_element(*MAIN_PAGE_LOGIN_BUTTON).click()

    driver.find_element(*LOGIN_EMAIL_FIELD).send_keys(exicting_user['email'])
    driver.find_element(*LOGIN_PASSWORD_FIELD).send_keys(exicting_user['password'])
    driver.find_element(*LOGIN_SUBMIT_BUTTON).click()

    WebDriverWait(driver, 5).until(EC.url_to_be("https://stellarburgers.education-services.ru/"))

    assert driver.find_element(By.XPATH, "//button[text()='Оформить заказ']").is_displayed()


def test_login_from_personal_account_button(driver, exicting_user):
    driver.get("https://stellarburgers.education-services.ru/")
    driver.find_element(*PERSONAL_ACCOUNT_BUTTON).click()

    driver.find_element(*LOGIN_EMAIL_FIELD).send_keys(exicting_user['email'])
    driver.find_element(*LOGIN_PASSWORD_FIELD).send_keys(exicting_user['password'])
    driver.find_element(*LOGIN_SUBMIT_BUTTON).click()

    WebDriverWait(driver, 5).until(EC.url_to_be("https://stellarburgers.education-services.ru/"))

    assert driver.find_element(By.XPATH, "//button[text()='Оформить заказ']").is_displayed()


def test_login_from_registration_form_button(driver, exicting_user):
    driver.get("https://stellarburgers.education-services.ru/register")
    driver.find_element(*FORMS_LOGIN_LINK).click()

    driver.find_element(*LOGIN_EMAIL_FIELD).send_keys(exicting_user['email'])
    driver.find_element(*LOGIN_PASSWORD_FIELD).send_keys(exicting_user['password'])
    driver.find_element(*LOGIN_SUBMIT_BUTTON).click()

    WebDriverWait(driver, 5).until(EC.url_to_be("https://stellarburgers.education-services.ru/"))

    assert driver.find_element(By.XPATH, "//button[text()='Оформить заказ']").is_displayed()


def test_login_from_password_reset_form_button(driver, exicting_user):
    driver.get("https://stellarburgers.education-services.ru/reset-password")
    driver.find_element(*FORMS_LOGIN_LINK).click()

    driver.find_element(*LOGIN_EMAIL_FIELD).send_keys(exicting_user['email'])
    driver.find_element(*LOGIN_PASSWORD_FIELD).send_keys(exicting_user['password'])
    driver.find_element(*LOGIN_SUBMIT_BUTTON).click()

    WebDriverWait(driver, 5).until(EC.url_to_be("https://stellarburgers.education-services.ru/"))

    assert driver.find_element(By.XPATH, "//button[text()='Оформить заказ']").is_displayed()