from pages.tables import Tables

def test_sort_columns(browser):
    page = Tables(browser)
    page.visit()

    headers = page.headers.find_elements()
    assert len(headers) > 0

    for header in headers:
        header.click()
        cls = header.get_attribute("class")
        assert "sorted" in cls or "rt-th" in cls