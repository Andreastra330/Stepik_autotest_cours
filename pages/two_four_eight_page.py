from conftest import driver
from pages.locators import *
from pages.base_page import BasePage
import math

class TestPage(BasePage):
    locators = LocatorsTwoFourEight
    def wait_and_click(self):
        self.text_present(self.locators.PRICE,"$100")
        self.click_element(self.locators.BTN_BOOK)
        calc = str(math.log(abs(12*math.sin(int(self.find_element(self.locators.VALUE).text)))))
        self.fill_input(self.locators.ANSWER,calc)
        self.click_element(self.locators.BTN_SUBMIT)