from selenium.webdriver.common.by import By


class AccordionPage:
    URL = "https://demoqa.com/accordian"

    def __init__(self, browser):
        self.browser = browser

    def load(self):
        self.browser.get(self.URL)

    # Элементы секции 1
    section1_heading = (By.CSS_SELECTOR, "#section1Heading")
    section1_content = (By.CSS_SELECTOR, "#section1Content > p")

    # Элементы секции 2
    section2_content_p1 = (By.CSS_SELECTOR, "#section2Content > p:nth-child(1)")
    section2_content_p2 = (By.CSS_SELECTOR, "#section2Content > p:nth-child(2)")

    # Элемент секции 3
    section3_content_p = (By.CSS_SELECTOR, "#section3Content > p")

    def get_element(self, locator):
        return self.browser.find_element(*locator)