from pages.two_one_five_page import TestPage
from conftest import driver
import time

def test_two_two_six(driver):
    course_page = TestPage(driver, "https://SunInJuly.github.io/execute_script.html")
    course_page.open()
    course_page.fill_and_click_btn()
    time.sleep(30)