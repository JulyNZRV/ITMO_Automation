import time
from pages.text_box import TextBox

import pytest
from selenium import webdriver


@pytest.fixture(scope="function")
def browser():
    driver = webdriver.Chrome()
    driver.set_window_size(1000, 1000)
    yield driver
    driver.quit()

def test_text_box(browser):
    tex_box_page = TextBox(browser)
    tex_box_page.visit()
    assert tex_box_page.name.get_dom_attribute("placeholder") == "Full Name"