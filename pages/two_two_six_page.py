from pages.locators import *
from pages.base_page import BasePage
import math

class TestPage(BasePage):
    locators = LocatorsTwoOneFive
    def fill_and_click_btn(self):
        calc = str(math.log(abs(12*math.sin(int(self.find_element(self.locators.VALUE).text)))))
        self.fill_input(self.locators.ANSWER,calc)
        self.click_element(self.locators.CHECKBOX)
        self.click_element(self.locators.RADIOBATTON)
        self.click_element(self.locators.BTN_SUBMIT)