from pages.base_page import BasePage
from components.components import WebElement


class Tables(BasePage):
    def __init__(self, driver):
        self.base_url = "https://demoqa.com/webtables"
        super().__init__(driver, self.base_url)

        self.btn_delete_row = WebElement(driver, 'span[title="Delete"]')
        self.no_data = WebElement(driver, 'div.rt-noData')

    def no_data_exist(self):
        return self.no_data.exist()


