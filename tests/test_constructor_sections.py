import pytest
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from locators import *


def test_move_to_fillings_sections_button(driver):
    driver.get("https://stellarburgers.education-services.ru/")
    driver.find_element(*FILLINGS_BUTTON).click()

    assert driver.find_element(By.XPATH, "//h2[text()='Начинки']").is_displayed()


def test_move_to_buns_section_button(driver):
    driver.get("https://stellarburgers.education-services.ru/")
    driver.find_element(*FILLINGS_BUTTON).click()
    driver.find_element(*BUNS_BUTTON).click()

    assert driver.find_element(By.XPATH, "//h2[text()='Булки']").is_displayed()


def test_move_to_sauces_section_button(driver):
    driver.get("https://stellarburgers.education-services.ru/")
    driver.find_element(*SAUCES_BUTTON).click()

    assert driver.find_element(By.XPATH, "//h2[text()='Соусы']").is_displayed()


