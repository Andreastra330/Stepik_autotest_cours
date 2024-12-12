from pages.locators import *
from pages.base_page import BasePage

class TestPage(BasePage):
    locators = LocatorsTwoTwoThree

    def choice_and_click_btn(self):
        num1 = self.find_element(self.locators.NUM1).text
        num2 = self.find_element(self.locators.NUM2).text
        self.click_element(self.locators.DROPDOWN)
        self.find_element_with_text(f"{int(num1) + int(num2)}").click()
        self.click_element(self.locators.BTN_SUBMIT)


