from selenium.webdriver.common.by import By
from pages.dynamic_locators import *

class LocatorsOneSix:
    FIRST_NAME = (By.NAME, "first_name")
    LAST_NAME = (By.NAME, "last_name")
    CITY = (By.CSS_SELECTOR, "input[class='form-control city']")
    COUNTRY = (By.ID, "country")
    BTN_SUBMIT = (By.ID, "submit_button")
    BTN_DEFAULT = (By.XPATH, "//*[text() = 'Submit']")
    NEED_VALUE = dynamic_value()
    TYPE_TEXT = (By.TAG_NAME, "input")



