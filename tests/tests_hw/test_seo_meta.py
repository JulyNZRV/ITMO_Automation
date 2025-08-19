from pages.demoqa import DemoQa
from pages.accordion import AccordionPage
from pages.alerts import Alerts
from pages.browser_tab import BrowserTab
import pytest
import time


@pytest.mark.parametrize('pages', [AccordionPage, Alerts, BrowserTab, DemoQa])
def test_check_title_all_pages(browser, pages):
    page = pages(browser)

    page.visit()
    time.sleep(2)
    assert page.metaView.exist()
    assert page.metaView.get_dom_attribute('name') == 'viewport'
    content = (page.metaView.get_dom_attribute('content') or '')
    assert content.replace(' ', '') == 'width=device-width,initial-scale=1'
