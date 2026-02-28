import pytest
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from locators import *


class TestConstructorTabs:

    def test_move_to_fillings_sections_button(self, driver):
        driver.get("https://stellarburgers.education-services.ru/")
        driver.find_element(*FILLINGS_BUTTON).click()

        WebDriverWait(driver, 5).until(EC.text_to_be_present_in_element((ACTIVE_TAB), 'Начинки'))

        assert driver.find_element(*ACTIVE_TAB).text == 'Начинки'

    def test_move_to_buns_section_button(self, driver):
        driver.get("https://stellarburgers.education-services.ru/")
        driver.find_element(*FILLINGS_BUTTON).click()
        driver.find_element(*BUNS_BUTTON).click()

        WebDriverWait(driver, 5).until(EC.text_to_be_present_in_element((ACTIVE_TAB), 'Булки'))

        assert driver.find_element(*ACTIVE_TAB).text == 'Булки'

    def test_move_to_sauces_section_button(self, driver):
        driver.get("https://stellarburgers.education-services.ru/")
        driver.find_element(*SAUCES_BUTTON).click()

        WebDriverWait(driver, 5).until(EC.text_to_be_present_in_element((ACTIVE_TAB), 'Соусы'))

        assert driver.find_element(*ACTIVE_TAB).text == 'Соусы'