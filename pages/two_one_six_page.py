from pages.locators import *
from pages.base_page import BasePage
import math

class TestPage(BasePage):
    locators = LocatorsTwoOneSix

    def fill_and_click_btn(self):
        value = self.get_attribute_element_value(self.locators.TREASURE,"valuex")
        calc = str(math.log(abs(12 * math.sin(int(value)))))
        self.fill_input(self.locators.ANSWER,calc)
        self.click_element(self.locators.CHECKBOX)
        self.click_element(self.locators.RADIOBATTON)
        self.click_element(self.locators.BTN_SUBMIT)


