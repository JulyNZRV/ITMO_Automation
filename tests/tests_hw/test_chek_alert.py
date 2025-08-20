import time
from pages.alerts import Alerts

def test_alert_check(browser):
    alerts_page = Alerts(browser)
    alerts_page.visit()

    alerts_page.timer_btn.click()
    time.sleep(6)  # через 5 сек после клика

    alert = alerts_page.alert()
    assert alert is not False
    assert "alert" in alert.text.lower()
    alert.accept()