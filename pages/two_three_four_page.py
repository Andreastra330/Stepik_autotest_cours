from conftest import driver
from pages.locators import *
from pages.base_page import BasePage
import math

class TestPage(BasePage):
    locators = LocatorsTwoThreeFour
    def btn_accept_fill_click(self):
        self.click_element(self.locators.BTN_FOR_ALERT)
        self.accept_allert()
        calc = str(math.log(abs(12*math.sin(int(self.find_element(self.locators.VALUE).text)))))
        self.fill_input(self.locators.ANSWER,calc)
        self.click_element(self.locators.BTN_SUBMIT)