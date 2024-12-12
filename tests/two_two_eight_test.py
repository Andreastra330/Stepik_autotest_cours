from pages.two_two_eight_page import TestPage
from conftest import driver
import time

def test_two_two_eight(driver):
    course_page = TestPage(driver, "https://suninjuly.github.io/file_input.html")
    course_page.open()
    course_page.fill_and_click_btn()
    time.sleep(30)