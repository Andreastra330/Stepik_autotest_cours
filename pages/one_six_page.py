from pages.locators import *
from pages.base_page import BasePage


class TestPage(BasePage):
    locators = LocatorsOneSix
    def fill_all_and_click_btn(self):
        self.fill_input(self.locators.FIRST_NAME,"Andrey")
        self.fill_input(self.locators.LAST_NAME,"Orlov")
        self.fill_input(self.locators.CITY,"Kurs")
        self.fill_input(self.locators.COUNTRY,"Russia")
        self.click_element(self.locators.BTN_SUBMIT)