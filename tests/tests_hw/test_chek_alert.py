import time
from pages.alerts import Alerts

def test_alert_check(browser):
    page = Alerts(browser)
    page.visit()

    page.timer_btn.click()
    time.sleep(6)  # через 5 сек после клика

    alert = page.alert()
    assert alert is not False
    assert "alert" in alert.text.lower()
    alert.accept()