from components.components import WebElement
from pages.base_page import BasePage

class ModalDialogs(BasePage):
    def __init__(self, driver):
        super().__init__(driver, "https://demoqa.com/modal-dialogs")
        self.menu_buttons = WebElement(driver, 'div.element-list > ul > li')
        self.main_icon = WebElement(driver, '#app > header > a')