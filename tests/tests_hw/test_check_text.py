from selenium.webdriver.common.by import By
from .components import WebText


def test_footer_text(browser):
    browser.get("https://demoqa.com")
    footer_component = WebText(browser, (By.CSS_SELECTOR, "footer span"))
    assert footer_component.get_text() == "© 2013-2020 TOOLSQA.COM | ALL RIGHTS RESERVED."


def test_central_text(browser):
    browser.get("https://demoqa.com")

    elements_button = WebText(browser, (By.CSS_SELECTOR, ".card:nth-child(1)"))
    elements_button.click()

    central_text_component = WebText(browser, (By.CSS_SELECTOR, ".col-12.mt-4.col-md-6"))
    assert central_text_component.get_text() == "Please select an item from left to start practice."