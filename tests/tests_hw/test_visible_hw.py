from pages.accordion import AccordionPage
import time

def test_visible_accordion(browser):
    page = AccordionPage(browser)
    page.load()

    content = page.get_element(AccordionPage.section1_content)
    assert content.is_displayed(), "Контент секции 1 должен быть видим"

    heading = page.get_element(AccordionPage.section1_heading)
    heading.click()

    time.sleep(2)

    assert not content.is_displayed(), "Контент секции 1 должен быть скрыт"

def test_visible_accordion_default(browser):
    page = AccordionPage(browser)
    page.load()

    elements = [
        page.get_element(AccordionPage.section2_content_p1),
        page.get_element(AccordionPage.section2_content_p2),
        page.get_element(AccordionPage.section3_content_p)
    ]

    for element in elements:
        assert not element.is_displayed(), f"Элемент {element} должен быть скрыт по умолчанию"