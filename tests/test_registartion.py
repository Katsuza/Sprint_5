import pytest
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from generators import generate_email, generate_password
from locators import *


class TestRegistration:

    def test_registation_correct_date_success(self, driver):
        driver.get("https://stellarburgers.education-services.ru/register")
        driver.find_element(*REGISTRATION_NAME_FIELD).send_keys('Artem')
        driver.find_element(*REGISTRATION_EMAIL_FIELD).send_keys(generate_email())
        driver.find_element(*REGISTRATION_PASSWORD_FIELD).send_keys(generate_password())

        driver.find_element(*REGISTRATION_SUMBIT_BUTTON).click()

        WebDriverWait(driver, 5).until(EC.url_to_be("https://stellarburgers.education-services.ru/login"))

        assert driver.current_url == 'https://stellarburgers.education-services.ru/login'

    def test_registartion_short_password_failure(self, driver):
        driver.get("https://stellarburgers.education-services.ru/register")
        driver.find_element(*REGISTRATION_NAME_FIELD).send_keys('Artem')
        driver.find_element(*REGISTRATION_EMAIL_FIELD).send_keys(generate_email())
        driver.find_element(*REGISTRATION_PASSWORD_FIELD).send_keys('12345')

        driver.find_element(*REGISTRATION_SUMBIT_BUTTON).click()

        assert driver.find_element(*INCORRECT_PASSWORD_TEXT).is_displayed()



