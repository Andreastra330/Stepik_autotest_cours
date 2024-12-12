from pages.two_one_five_page import TestPage
from conftest import driver
import time




def test_onesix_2(driver):
    course_page = TestPage(driver, "https://suninjuly.github.io/math.html")
    course_page.open()
    course_page.fill_and_click_btn()
    time.sleep(30)