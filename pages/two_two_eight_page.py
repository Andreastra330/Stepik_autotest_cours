from pages.locators import *
from pages.base_page import BasePage


class TestPage(BasePage):
    locators = LocatorsTwoTwoEight
    def fill_and_click_btn(self):
        self.fill_input(self.locators.FIRST_NAME,"Andrey")
        self.fill_input(self.locators.LAST_NAME,"ORLOV")
        self.fill_input(self.locators.EMAIL,"@.ru")
        self.put_file(self.locators.FILE,"C:/readme.txt")
        self.click_element(self.locators.BTN_SUBMIT)