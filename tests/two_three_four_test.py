from pages.two_three_four_page import TestPage
from conftest import driver
import time

def test_two_three_four(driver):
    course_page = TestPage(driver, "http://suninjuly.github.io/alert_accept.html")
    course_page.open()
    course_page.btn_accept_fill_click()
    time.sleep(30)