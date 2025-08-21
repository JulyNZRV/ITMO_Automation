from pages.slider import Slider
from selenium.webdriver.common.keys import Keys

def test_slider_page(browser):
    page = Slider(browser)

    page.visit()
    assert page.slider.exist()
    assert page.inp.exist()

    while not page.inp.get_dom_attribute("value") == "50":
         page.slider.send_keys(Keys.ARROW_RIGHT)

    assert page.inp.get_dom_attribute("value") == "50"