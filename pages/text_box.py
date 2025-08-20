from pages.base_page import BasePage
from components.components import WebElement


class TextBox(BasePage):

    def __init__(self, driver):
        self.base_url = "https://demoqa.com/text-box"
        super().__init__(driver, self.base_url)

        self.name = WebElement(driver, "#userName")
        self.email = WebElement(driver, "#userEmail")
        self.current_address = WebElement(driver, "#currentAddress")
        self.permanent_address = WebElement(driver, "#permanentAddress")
        self.submit_btn = WebElement(driver, "#submit")


        self.output_name = WebElement(driver, "#output #name")
        self.output_email = WebElement(driver, "#output #email")
        self.output_current_address = WebElement(driver, "#output #currentAddress")
        self.output_permanent_address = WebElement(driver, "#output #permanentAddress")