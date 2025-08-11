from base_page import BasePage
from components.components import  WebElement, WebElements

class ModalDialogsPage(BasePage):
    def __init__(self, driver):
        super().__init__(driver, "https://demoqa.com/modal-dialogs")
        self.menu_buttons = WebElements(driver, 'div.element-list > ul > li')
        self.main_icon = WebElements(driver, '#app > header > a')