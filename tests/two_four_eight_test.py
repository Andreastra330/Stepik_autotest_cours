from pages.two_four_eight_page import TestPage
from conftest import driver
import time

def test_two_four_eight(driver):
    course_page = TestPage(driver, "https://suninjuly.github.io/explicit_wait2.html")
    course_page.open()
    course_page.wait_and_click()
    time.sleep(30)