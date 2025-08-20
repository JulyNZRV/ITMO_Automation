import time
from pages.text_box import TextBox

def test_text_box(browser):
    tex_box_page = TextBox(browser)
    tex_box_page.visit()
    assert tex_box_page.name.get_dom_attribute("placeholder") == "Full Name"


def test_text_box_submission(browser):
    text_box_page = TextBox(browser)
    text_box_page.visit()

    full_name = "July"
    current_address = "Невский проспект д.23"

    text_box_page.name.send_keys(full_name)
    text_box_page.current_address.send_keys(current_address)

    text_box_page.submit_btn.click()
    time.sleep(2)

    assert text_box_page.output_name.get_text() == f"Name:{full_name}"
    assert text_box_page.output_current_address.get_text() == f"Current Address :{current_address}"