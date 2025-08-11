from .base_page import BasePage
from components.components import WebElement


class LoginForm(BasePage):
    def __init__(self, driver):
        super().__init__(driver, "https://demoqa.com/automation-practice-form")

        self.first_name = WebElement(driver, "#firstName")
        self.last_name = WebElement(driver, "#lastName")
        self.user_email = WebElement(driver, "#userEmail")
        self.submit_btn = WebElement(driver, "#submit")
        self.form = WebElement(driver, "#userForm")