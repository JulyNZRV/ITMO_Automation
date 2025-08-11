

from selenium.webdriver.common.by import By
from selenium.common.exceptions import NoSuchElementException

class WebElement:
    def __init__(self, driver, locator):
        self.driver = driver
        self.locator = locator
        self.element = None

    def find_element(self):
        if not self.element:
            self.element = self.driver.find_element(By.CSS_SELECTOR, self.locator)
        return self.element

    def find_elements(self):
        return self.driver.find_elements(By.CSS_SELECTOR, self.locator)

    def click(self):
        self.find_element().click()

    def get_text(self):
        return str(self.find_element().text)

    def exist(self):
        try:
            self.find_element()
            return True
        except NoSuchElementException:
            return False

    def visible(self):
        return self.find_element().is_displayed()

    def check_count_elements(self, count: int) -> bool:
        if len(self.find_elements()) == count:
            return True
        return False

    def send_keys(self, text: str):
        self.find_element().send_keys(text)


class WebElements:
    def __init__(self, driver, locator):
        self.driver = driver
        self.locator = locator
        self.elements = driver.find_elements(By.CSS_SELECTOR, locator)

    def __len__(self):
        return len(self.elements)

    def click_first(self):
        if self.elements:
            self.elements[0].click()