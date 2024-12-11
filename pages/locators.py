from selenium.webdriver.common.by import By


class LocatorsOneSix:
    FIRST_NAME = (By.NAME, "first_name")
    LAST_NAME = (By.NAME, "last_name")
    CITY = (By.CSS_SELECTOR, "input[class='form-control city']")
    COUNTRY = (By.ID, "country")
    BTN_SUBMIT = (By.ID, "submit_button")