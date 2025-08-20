import time
from pages.tables import Tables
from selenium.webdriver.common.by import By



def test_tables(browser):
    """Проверка блока No rows found"""
    page_tables = Tables(browser)

    page_tables.visit()
    assert not page_tables.no_data.exist()

    # Удаляем все записи
    while True:
        rows = browser.find_elements(By.CSS_SELECTOR, "span[title='Delete']")
        if not rows:
            break
        rows[0].click()

    time.sleep(1)
    assert page_tables.no_data.exist()


def test_webtables_crud(browser):
    page = Tables(browser)
    page.visit()
    time.sleep(3)

    data = {
        "first_name": "Ivan",
        "last_name": "Petrov",
        "user_email": "ivan.petrov@example.com",
        "age": "30",
        "salary": "5000",
        "department": "QA",
    }
    page.add_record(data)
    time.sleep(3)
    assert page.record_exists("Ivan")

    # UPDATE
    new_data = {
        "first_name": "Sergey",
        "last_name": "Ivanov",
        "user_email": "sergey.ivanov@example.com",
        "age": "35",
        "salary": "7000",
        "department": "Dev",
    }
    page.edit_record("Ivan", new_data)
    time.sleep(3)
    assert page.record_exists("Sergey")

    #DELETE
    page.delete_record("Sergey")
    time.sleep(1)
    assert not page.record_exists("Sergey")