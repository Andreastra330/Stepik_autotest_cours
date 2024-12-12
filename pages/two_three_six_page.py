from conftest import driver
from pages.locators import *
from pages.base_page import BasePage
import math

class TestPage(BasePage):
    locators = LocatorsTwoThreeSix
    def btn_fill_click(self):
        self.click_element(self.locators.MOVE_BUTTON)
        self.switch_to_next_tab()
        calc = str(math.log(abs(12*math.sin(int(self.find_element(self.locators.VALUE).text)))))
        self.fill_input(self.locators.ANSWER,calc)
        self.click_element(self.locators.BTN_SUBMIT)