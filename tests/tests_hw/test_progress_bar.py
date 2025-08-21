from pages.progress_bar import ProgressBar
import time

def test_progress_bar(browser):
    page = ProgressBar(browser)
    page.visit()
    time.sleep(2)

    page.button.click()

    while True:
        if page.bar.get_dom_attribute("aria-valuenow") == "51":
            page.button.click()
            break


