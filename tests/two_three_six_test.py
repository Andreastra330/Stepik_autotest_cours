from pages.two_three_six_page import TestPage
from conftest import driver
import time

def test_two_three_six(driver):
    course_page = TestPage(driver, "http://suninjuly.github.io/redirect_accept.html")
    course_page.open()
    course_page.btn_fill_click()
    time.sleep(30)