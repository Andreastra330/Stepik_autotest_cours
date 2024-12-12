from pages.locators import *
from pages.base_page import BasePage


class TestPage(BasePage):
    locators = LocatorsForOneSixTen
    def fill_all_and_click_btn(self):
        self.fill_input(self.locators.FIRST_NAME,"Моё")
        self.fill_input(self.locators.LAST_NAME,"Моё")
        self.fill_input(self.locators.EMAIL,"Моё")
        self.fill_input(self.locators.PHONE,"ASD")
        self.fill_input(self.locators.ADDRESS,"qwe")
        self.click_element(self.locators.BTN_DEFAULT)

    def get_text(self):
         return self.find_element(self.locators.TEXT).text



