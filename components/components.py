#
from selenium.webdriver.common.by import By
from selenium.common.exceptions import NoSuchElementException, StaleElementReferenceException, TimeoutException
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC


class WebElement:
    def __init__(self, driver, locator):
        self.driver = driver
        self.locator = locator  # CSS

    def _by(self):
        return (By.CSS_SELECTOR, self.locator)

    def find_element(self):
        # Всегда ищем заново — не кешируем, иначе будут stale-element
        return self.driver.find_element(*self._by())

    def find_elements(self):
        return self.driver.find_elements(*self._by())

    def click(self, timeout: int = 5):
        wait = WebDriverWait(self.driver, timeout)
        try:
            el = wait.until(EC.element_to_be_clickable(self._by()))
            el.click()
        except StaleElementReferenceException:
            # повторная попытка, если DOM успел перерисоваться
            el = wait.until(EC.element_to_be_clickable(self._by()))
            el.click()

    def get_text(self):
        try:
            return str(self.find_element().text)
        except StaleElementReferenceException:
            return str(self.find_element().text)

    def exist(self, timeout: int = 0) -> bool:
        # presence в DOM (не обязательно видим)
        if timeout:
            try:
                WebDriverWait(self.driver, timeout).until(
                    EC.presence_of_element_located(self._by())
                )
                return True
            except TimeoutException:
                return False
        try:
            self.driver.find_element(*self._by())
            return True
        except NoSuchElementException:
            return False

    def visible(self, timeout: int = 0) -> bool:
        # видимость элемента
        if timeout:
            try:
                WebDriverWait(self.driver, timeout).until(
                    EC.visibility_of_element_located(self._by())
                )
                return True
            except TimeoutException:
                return False
        try:
            return self.find_element().is_displayed()
        except (NoSuchElementException, StaleElementReferenceException):
            return False

    def check_count_elements(self, count: int) -> bool:
        return len(self.find_elements()) == count

    def send_keys(self, text: str):
        el = self.find_element()
        try:
            el.clear()
        except Exception:
            pass
        el.send_keys(text)

    def clear(self):
        try:
            self.find_element().clear()
        except StaleElementReferenceException:
            self.find_element().clear()

    def value(self):
        # удобно для <input> — получить текущее значение
        return self.find_element().get_attribute("value")

