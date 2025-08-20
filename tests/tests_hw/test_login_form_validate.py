import time
from pages.login_gorm_validate import LoginForm


def test_form_placeholders(browser):
    form_page = LoginForm(browser)
    form_page.visit()

    assert form_page.first_name.get_dom_attribute("placeholder") == "First Name"
    assert form_page.last_name.get_dom_attribute("placeholder") == "Last Name"
    assert form_page.user_email.get_dom_attribute("placeholder") == "name@example.com"

    assert form_page.user_email.get_dom_attribute(
        "pattern") == '^([a-zA-Z0-9_\\-\\.]+)@([a-zA-Z0-9_\\-\\.]+)\\.([a-zA-Z]{2,5})$'


def test_form_validation(browser):
    form_page = LoginForm(browser)
    form_page.visit()

    form_page.submit_btn.click_force()
    time.sleep(2)

