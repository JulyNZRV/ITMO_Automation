from components.components import WebElement
from pages.base_page import BasePage

class ModalDialogs(BasePage):
    def __init__(self, driver):
        super().__init__(driver, "https://demoqa.com/modal-dialogs")
        self.menu_buttons = WebElement(driver, 'div.element-list > ul > li')
        self.main_icon = WebElement(driver, '#app > header > a')

        self.btn_small = WebElement(driver, "#showSmallModal")
        self.btn_large = WebElement(driver, "#showLargeModal")
        self.btn_close_small = WebElement(driver, "#closeSmallModal")
        self.btn_close_large = WebElement(driver, "#closeLargeModal")