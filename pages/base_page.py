from selenium.webdriver import Keys
import os
from datetime import datetime
import time
import re
from selenium.webdriver.support.wait import WebDriverWait
import sys
from pages.locators import *
from selenium.webdriver.support.ui import WebDriverWait as wait
from selenium.webdriver.support import expected_conditions as EC

class BasePage:
    def __init__(self, driver,url):
        self.driver = driver
        self.url = url

    def open(self):
        self.driver.get(self.url)

    def find_element(self, locator, timeout=60):
        element = WebDriverWait(self.driver, timeout).until(EC.presence_of_element_located(locator))
        self.driver.execute_script("arguments[0].scrollIntoView()", element)
        return element

    def fill_input(self, locator, sending_text: str, timeout=60):
        element = WebDriverWait(self.driver, timeout).until(EC.presence_of_element_located(locator))
        self.driver.execute_script("arguments[0].scrollIntoView()", element)
        self.find_element(locator).send_keys(sending_text)

    def click_element(self,locator):
        return self.driver.find_element(*locator).click()