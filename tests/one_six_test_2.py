from pages.one_six_two_page import TestPage
from conftest import driver
import time




def test_one_six_2(driver):
    course_page = TestPage(driver, "https://suninjuly.github.io/find_link_text")
    course_page.open()
    course_page.find_element_and_click()
    course_page.fill_all_and_click_btn()
    time.sleep(30)
