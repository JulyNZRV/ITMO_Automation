from pages.form_page import FormPage
from selenium.webdriver.common.by import By  # Добавьте этот импорт
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
#import time
#
# def test_login_form(browser):
#     form_page = FormPage(browser)
#
#     form_page.visit()
#     assert not form_page.modal_dialog.exist()
#     #time.sleep(3)
#     form_page.first_name.send_keys("tester")
#     form_page.last_name.send_keys("testovich")
#     form_page.user_email.send_keys("test@gmail.com")
#     WebDriverWait(browser, 10).until(
#         EC.element_to_be_clickable(form_page.gender_radio_1.locator)
#     ).click()
#     form_page.user_number.send_keys("9031963851")
#     #time.sleep(3)
#     form_page.btn_submit.click()
#     #time.sleep(3)


def test_login_form(browser):
    form_page = FormPage(browser)

    form_page.visit()
    assert not form_page.modal_dialog.exist()

    form_page.first_name.send_keys("tester")
    form_page.last_name.send_keys("testovich")
    form_page.user_email.send_keys("test@gmail.com")

    WebDriverWait(browser, 10).until(
        EC.element_to_be_clickable(
            (By.CSS_SELECTOR, form_page.gender_radio_1.locator)  # Теперь By определен
        )
    ).click()

    form_page.user_number.send_keys("9031963851")
    browser.execute_script("arguments[0].scrollIntoView(true);", form_page.btn_submit.find_element())
    WebDriverWait(browser, 10).until(
        EC.element_to_be_clickable(
            (By.CSS_SELECTOR, form_page.btn_submit.locator)
        )
    )

    # Клик через JavaScript
    browser.execute_script("arguments[0].click();", form_page.btn_submit.find_element())