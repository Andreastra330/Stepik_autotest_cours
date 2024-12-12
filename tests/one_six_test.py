from pages.one_six_page import TestPage
from conftest import driver
import time



def test_one_six_1(driver):
    course_page = TestPage(driver, "https://suninjuly.github.io/simple_form_find_task.html")
    course_page.open()
    course_page.fill_all_and_click_btn()
    time.sleep(30)
