from selenium.webdriver.common.by import By
from pages.base_page import BasePage


class AccordionPage(BasePage):
    def __init__(self, driver):
        self.base_url = "https://demoqa.com/accordian"
        super().__init__(driver, self.base_url)

    section1_heading = (By.CSS_SELECTOR, "#section1Heading")
    section1_content = (By.CSS_SELECTOR, "#section1Content > p")

    section2_content_p1 = (By.CSS_SELECTOR, "#section2Content > p:nth-child(1)")
    section2_content_p2 = (By.CSS_SELECTOR, "#section2Content > p:nth-child(2)")

    section3_content_p = (By.CSS_SELECTOR, "#section3Content > p")







