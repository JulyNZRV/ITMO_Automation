import time
from pages.accordion import AccordionPage


def test_visible_accordion(browser):
    # Инициализация и переход на страницу
    page = AccordionPage(browser)
    page.load()

    # Проверка видимости контента секции 1
    content = page.get_element(AccordionPage.section1_content)
    assert content.is_displayed(), "Контент секции 1 должен быть видим"

    # Клик по заголовку секции 1
    heading = page.get_element(AccordionPage.section1_heading)
    heading.click()

    # Пауза для анимации
    time.sleep(2)

    # Проверка скрытия контента секции 1
    assert not content.is_displayed(), "Контент секции 1 должен быть скрыт"


def test_visible_accordion_default(browser):
    # Инициализация и переход на страницу
    page = AccordionPage(browser)
    page.load()

    # Проверка скрытых элементов по умолчанию
    elements = [
        page.get_element(AccordionPage.section2_content_p1),
        page.get_element(AccordionPage.section2_content_p2),
        page.get_element(AccordionPage.section3_content_p)
    ]

    for element in elements:
        assert not element.is_displayed(), f"Элемент {element} должен быть скрыт по умолчанию"