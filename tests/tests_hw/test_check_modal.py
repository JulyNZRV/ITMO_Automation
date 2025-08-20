import pytest
import requests
import time
from pages.modal_dialogs import ModalDialogs

URL = "https://demoqa.com/modal-dialogs"


def test_check_modals(browser):
    # *тест пропускается, если страница недоступна
    try:
        resp = requests.get(URL, timeout=5)
        if resp.status_code != 200:
            pytest.skip(f"Page unavailable, status code {resp.status_code}")
    except requests.RequestException:
        pytest.skip("Page unavailable")

    modal_dialogs_page = ModalDialogs(browser)
    modal_dialogs_page.visit()
    time.sleep(3)

    # на странице присутствуют 2 кнопки “Small modal” и “Large modal”
    assert modal_dialogs_page.btn_small.exist(3)
    assert modal_dialogs_page.btn_large.exist(3)

    #  Small modal
    modal_dialogs_page.btn_small.click()
    time.sleep(3)
    modal_dialogs_page.btn_close_small.click()
    time.sleep(3)

    # Large modal
    modal_dialogs_page.btn_large.click()
    time.sleep(3)
    modal_dialogs_page.btn_close_large.click()
    time.sleep(3)
