from pages.one_six_seven import TestPage
from conftest import driver
import time




def test_onesix_2(driver):
    course_page = TestPage(driver, "https://suninjuly.github.io/huge_form.html")
    course_page.open()
    course_page.fill_all_and_click_btn()

    time.sleep(30)
