import time
from pages.modal_dialogs import ModalDialogs
from pages.demoqa import DemoQa


import pytest
from selenium import webdriver


@pytest.fixture(scope="function")
def browser():
    driver = webdriver.Chrome()
    driver.set_window_size(1000, 1000)
    yield driver
    driver.quit()


def test_modal_elements(browser):
    modal_page = ModalDialogs(browser)
    modal_page.visit()

    assert len(modal_page.menu_buttons) == 5


def test_navigation_modal(browser):
    modal_page = ModalDialogs(browser)
    main_page = DemoQa(browser)

    modal_page.visit()
    modal_page.refresh()
    modal_page.main_icon.click()
    modal_page.back()
    modal_page.set_window_size(900, 400)
    modal_page.forward()
    time.sleep(2)

    assert main_page.get_url() == main_page.base_url

    assert main_page.get_title() == "DEMOQA"

    modal_page.set_window_size(1000, 1000)