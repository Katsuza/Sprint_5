import pytest
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from locators import *


class TestNavigation:

    def test_transition_to_personal_account_page(self, logged_user):
        driver = logged_user
        driver.find_element(*PERSONAL_ACCOUNT_BUTTON).click()

        WebDriverWait(driver, 5).until(EC.url_to_be("https://stellarburgers.education-services.ru/account/profile"))

        assert driver.current_url == "https://stellarburgers.education-services.ru/account/profile"

    def test_transaction_to_costructor_page_by_clicking_constructor_button(self, logged_user):
        driver = logged_user
        driver.find_element(*PERSONAL_ACCOUNT_BUTTON).click()

        WebDriverWait(driver, 5).until(EC.visibility_of_element_located(CONSTRUCTOR_LINK_BUTTON))

        driver.find_element(*CONSTRUCTOR_LINK_BUTTON).click()

        assert driver.find_element(By.CLASS_NAME, "BurgerIngredients_ingredients__1N8v2").is_displayed()

    def test_transaction_to_costructor_page_by_clicking_logo(self, logged_user):
        driver = logged_user
        driver.find_element(*PERSONAL_ACCOUNT_BUTTON).click()

        WebDriverWait(driver, 5).until(EC.visibility_of_element_located(LOGO_BUTTON))

        driver.find_element(*LOGO_BUTTON).click()

        assert driver.find_element(By.CLASS_NAME, "BurgerIngredients_ingredients__1N8v2").is_displayed()

    def test_logout_by_clicking_logout_button(self, logged_user):
        driver = logged_user
        driver.find_element(*PERSONAL_ACCOUNT_BUTTON).click()

        WebDriverWait(driver, 5).until(EC.visibility_of_element_located(LOGOUT_BUTTON))

        driver.find_element(*LOGOUT_BUTTON).click()

        WebDriverWait(driver, 5).until(EC.url_changes("https://stellarburgers.education-services.ru/account/profile"))

        assert driver.current_url == "https://stellarburgers.education-services.ru/login"

