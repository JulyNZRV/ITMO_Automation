from pages.base_page import BasePage
from components.components import WebElement

class Radio(BasePage):

    def __init__(self, driver):
        self.base_url = "https://demoqa.com/radio-button"
        super().__init__(driver, self.base_url)

        self.yes = WebElement(driver, "label[for='yesRadio']")
        self.impressive = WebElement(driver, "label[for='impressiveRadio']")
        self.no = WebElement(driver, "#noRadio")
        self.text = WebElement(driver, "span.text-success")
