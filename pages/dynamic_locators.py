from selenium.webdriver.common.by import By
import math

def dynamic_value():
    link = str(math.ceil(math.pow(math.pi, math.e) * 10000))
    return (By.XPATH, f"//*[text() = '{link}']")