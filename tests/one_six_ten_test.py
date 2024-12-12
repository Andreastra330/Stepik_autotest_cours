from pages.one_six_ten_page import TestPage
from conftest import driver
import time




def test_onesix_2(driver):
    course_page = TestPage(driver, "https://suninjuly.github.io/registration1.html")
    course_page.open()
    course_page.fill_all_and_click_btn()
    time.sleep(2)
    text = course_page.get_text()
    assert "Congratulations! You have successfully registered!" == text
    time.sleep(2)

def test_onesix_3(driver):
    course_page = TestPage(driver, "https://suninjuly.github.io/registration2.html")
    course_page.open()
    course_page.fill_all_and_click_btn()
    time.sleep(2)
    text = course_page.get_text()
    assert "Congratulations! You have successfully registered!" == text
    time.sleep(2)