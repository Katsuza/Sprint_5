import pytest
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from locators import *


class TestRegistration:

    def test_move_to_fillings_sections_button(self, driver):
        driver.get("https://stellarburgers.education-services.ru/")
        button = driver.find_element(*FILLINGS_BUTTON)
        parent = button.find_element(*FILLINGS_BUTTON_PARENT)

        button.click()

        WebDriverWait(driver, 5).until(EC.text_to_be_present_in_element_attribute((FILLINGS_BUTTON_PARENT), 'class', 'tab_tab_type_current'))

        assert "tab_tab_type_current" in parent.get_attribute("class")

    def test_move_to_buns_section_button(self, driver):
        driver.get("https://stellarburgers.education-services.ru/")
        driver.find_element(*FILLINGS_BUTTON).click()
        button = driver.find_element(*BUNS_BUTTON)
        parent = driver.find_element(*BUNS_BUTTON_PARENT)

        button.click()

        WebDriverWait(driver, 5).until(EC.text_to_be_present_in_element_attribute((BUNS_BUTTON_PARENT), 'class', 'tab_tab_type_current'))

        assert "tab_tab_type_current" in parent.get_attribute("class")

    def test_move_to_sauces_section_button(self, driver):
        driver.get("https://stellarburgers.education-services.ru/")
        button = driver.find_element(*SAUCES_BUTTON)
        parent = driver.find_element(*SAUCES_BUTTON_PARENT)

        button.click()

        WebDriverWait(driver, 5).until(EC.text_to_be_present_in_element_attribute((SAUCES_BUTTON_PARENT), 'class', 'tab_tab_type_current'))

        assert "tab_tab_type_current" in parent.get_attribute("class")
