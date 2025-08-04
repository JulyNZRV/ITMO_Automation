
class WebText:
    def __init__(self, driver, locator):
        self.driver = driver
        self.locator = locator
        self.element = None

    def find_element(self):
        if not self.element:
            self.element = self.driver.find_element(*self.locator)
        return self.element

    def click(self):
        self.find_element().click()

    def get_text(self):
        return str(self.find_element().text)