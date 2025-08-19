from pages.accordion import AccordionPage
import time

def test_visible_accordion(browser):
    page = AccordionPage(browser)
    page.visit()

    content = page.find_element("#section1Content > p")
    assert content.is_displayed(), "Контент секции 1 должен быть видим"

    heading = page.find_element("#section1Heading")
    heading.click()

    time.sleep(2)
    assert not content.is_displayed(), "Контент секции 1 должен быть скрыт"


def test_visible_accordion_default(browser):
    page = AccordionPage(browser)
    page.visit()

    elements = [
        page.find_element("#section2Content > p:nth-child(1)"),
        page.find_element("#section2Content > p:nth-child(2)"),
        page.find_element("#section3Content > p")
    ]

    for element in elements:
        assert not element.is_displayed(), f"Элемент {element} должен быть скрыт по умолчанию"