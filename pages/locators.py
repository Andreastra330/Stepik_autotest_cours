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

class LocatorsForOneSixTen:
    FIRST_NAME = (By.CSS_SELECTOR, "input[placeholder='Input your first name']")
    LAST_NAME = (By.CSS_SELECTOR, "input[placeholder='Input your last name']")
    EMAIL = (By.CSS_SELECTOR, "input[placeholder='Input your email']")
    PHONE = (By.CSS_SELECTOR, "input[placeholder='Input your phone:']")
    ADDRESS = (By.CSS_SELECTOR, "input[placeholder='Input your address:']")
    BTN_DEFAULT = (By.XPATH, "//*[text() = 'Submit']")
    TEXT = (By.CSS_SELECTOR, "h1")

class LocatorsTwoOneFive:
    VALUE = (By.ID, "input_value")
    ANSWER = (By.ID, "answer")
    CHECKBOX = (By.ID, "robotCheckbox")
    RADIOBATTON = (By.ID, "robotsRule")
    BTN_SUBMIT = (By.XPATH, "//*[text() = 'Submit']")

class LocatorsTwoOneSix:
    TREASURE = (By.ID, "treasure")
    ANSWER = (By.ID, "answer")
    CHECKBOX = (By.ID, "robotCheckbox")
    RADIOBATTON = (By.ID, "robotsRule")
    BTN_SUBMIT = (By.XPATH, "//*[text() = 'Submit']")

class LocatorsTwoTwoThree:
    NUM1 = (By.CSS_SELECTOR, "#num1")
    NUM2 = (By.CSS_SELECTOR, "#num2")
    DROPDOWN = (By.CSS_SELECTOR, "#dropdown")
    BTN_SUBMIT = (By.XPATH, "//*[text() = 'Submit']")

class LocatorsTwoTwoEight:
    FIRST_NAME = (By.NAME, "firstname")
    LAST_NAME = (By.NAME, "lastname")
    EMAIL = (By.NAME, "email")
    FILE = (By.ID, "file")
    BTN_SUBMIT = (By.XPATH, "//*[text() = 'Submit']")

class LocatorsTwoThreeFour:
    BTN_FOR_ALERT = (By.XPATH, "//*[text() = 'I want to go on a magical journey!']")
    VALUE = (By.ID, "input_value")
    ANSWER = (By.ID, "answer")
    BTN_SUBMIT = (By.XPATH, "//*[text() = 'Submit']")

class LocatorsTwoThreeSix:
    MOVE_BUTTON = (By.CSS_SELECTOR, "button")
    VALUE = (By.ID, "input_value")
    ANSWER = (By.ID, "answer")
    BTN_SUBMIT = (By.XPATH, "//*[text() = 'Submit']")

class LocatorsTwoFourEight:
    PRICE = (By.ID, "price")
    BTN_BOOK = (By.ID, "book")
    VALUE = (By.ID, "input_value")
    ANSWER = (By.ID, "answer")
    BTN_SUBMIT = (By.XPATH, "//*[text() = 'Submit']")