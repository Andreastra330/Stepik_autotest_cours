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
from selenium.webdriver.remote.switch_to import SwitchTo

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

    def find_elements_and_fill(self, locator, timeout=60):
        elements = WebDriverWait(self.driver, timeout).until(EC.presence_of_all_elements_located(locator))
        for element in elements:
            self.driver.execute_script("arguments[0].scrollIntoView()", element)
            element.send_keys("Моё")
        return elements

    def fill_input(self, locator, sending_text: str, timeout=60):
        element = WebDriverWait(self.driver, timeout).until(EC.presence_of_element_located(locator))
        self.driver.execute_script("arguments[0].scrollIntoView()", element)
        self.find_element(locator).send_keys(sending_text)

    def click_element(self,locator):
        return self.driver.find_element(*locator).click()

    def get_attribute_element(self,locator):
        element = self.find_element(locator)
        return element

    def get_attribute_element_value(self,locator,attribute="value"):
        element = self.find_element(locator)
        value = element.get_attribute(attribute)
        return value

    def find_element_with_text(self,text,timeout=60):
        element= WebDriverWait(self.driver, timeout).until(EC.presence_of_element_located((By.XPATH, f"//*[text() = '{text}']")))
        self.driver.execute_script("arguments[0].scrollIntoView()", element)
        return element

    def put_file(self,locator,path):
        return self.driver.find_element(*locator).send_keys(path)

    def accept_allert(self):
        self.driver.switch_to.alert.accept()

    def dismiss_allert(self):
        self.driver.switch_to.alert.dismiss()

    def switch_to_next_tab(self):
        self.driver.switch_to.window(self.driver.window_handles[1])

    def text_present(self,locator,text,timeout=60):
        element= WebDriverWait(self.driver, timeout).until(EC.text_to_be_present_in_element(locator,f"{text}"))
        return element