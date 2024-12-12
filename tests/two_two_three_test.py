from pages.two_two_three_page import TestPage
from conftest import driver
import time

def test_two_one_seven(driver):
    course_page = TestPage(driver, "https://suninjuly.github.io/selects1.html")
    course_page.open()
    course_page.choice_and_click_btn()
    time.sleep(30)