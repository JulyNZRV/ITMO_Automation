from selenium.webdriver.common.by import By

class WebElement:
    def __init__(self, driver, locator):
        self.driver = driver
        self.locator = locator
        self.element = None

    def find_element(self):
        if not self.element:
            self.element = self.driver.find_element(By.CSS_SELECTOR, self.locator)
        return self.element

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
