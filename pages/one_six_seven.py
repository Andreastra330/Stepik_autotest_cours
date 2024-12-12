from pages.locators import *
from pages.base_page import BasePage


class TestPage(BasePage):
    locators = LocatorsOneSix
    def fill_all_and_click_btn(self):
        self.find_elements_and_fill(self.locators.TYPE_TEXT)
        self.click_element(self.locators.BTN_DEFAULT)