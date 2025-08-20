from pages.base_page import BasePage
from components.components import WebElement
from selenium.webdriver.common.by import By


class Tables(BasePage):
    def __init__(self, driver):
        self.base_url = "https://demoqa.com/webtables"
        super().__init__(driver, self.base_url)

        #заголовки столбца страницы
        self.headers = WebElement(driver, ".rt-th")

        # кнопки
        self.btn_add = WebElement(driver, "#addNewRecordButton")
        self.btn_submit = WebElement(driver, "#submit")

        # модалка
        self.modal = WebElement(driver, ".modal-content")

        # поля формы
        self.first_name = WebElement(driver, "#firstName")
        self.last_name = WebElement(driver, "#lastName")
        self.user_email = WebElement(driver, "#userEmail")
        self.age = WebElement(driver, "#age")
        self.salary = WebElement(driver, "#salary")
        self.department = WebElement(driver, "#department")

        # таблица
        self.table = WebElement(driver, ".rt-tbody")
        self.no_data = WebElement(driver, "div.rt-noData")

    # ============ CRUD helper methods ============
    def add_record(self, data: dict):
        """Добавление новой записи"""
        self.btn_add.click()
        self.first_name.send_keys(data["first_name"])
        self.last_name.send_keys(data["last_name"])
        self.user_email.send_keys(data["user_email"])
        self.age.send_keys(data["age"])
        self.salary.send_keys(data["salary"])
        self.department.send_keys(data["department"])
        self.btn_submit.click()

    def get_row_by_name(self, name: str):
        """Ищет строку таблицы по имени"""
        rows = self.driver.find_elements(By.CSS_SELECTOR, ".rt-tr-group")
        for row in rows:
            if name in row.text:
                return row
        return None

    def edit_record(self, old_name: str, new_data: dict):
        """Редактирование записи по имени"""
        row = self.get_row_by_name(old_name)
        if not row:
            raise ValueError(f"Запись '{old_name}' не найдена")
        edit_btn = row.find_element(By.CSS_SELECTOR, 'span[title="Edit"]')
        edit_btn.click()

        # чистим поля и вводим новые данные
        self.first_name.find_element().clear()
        self.first_name.send_keys(new_data["first_name"])
        self.last_name.find_element().clear()
        self.last_name.send_keys(new_data["last_name"])
        self.user_email.find_element().clear()
        self.user_email.send_keys(new_data["user_email"])
        self.age.find_element().clear()
        self.age.send_keys(new_data["age"])
        self.salary.find_element().clear()
        self.salary.send_keys(new_data["salary"])
        self.department.find_element().clear()
        self.department.send_keys(new_data["department"])



        self.btn_submit.click()

    def delete_record(self, name: str):
        """Удаление записи по имени"""
        row = self.get_row_by_name(name)
        if not row:
            raise ValueError(f"Запись '{name}' не найдена")
        delete_btn = row.find_element(By.CSS_SELECTOR, 'span[title="Delete"]')
        delete_btn.click()

    def record_exists(self, name: str) -> bool:
        """Проверка, есть ли запись в таблице"""
        return self.get_row_by_name(name) is not None