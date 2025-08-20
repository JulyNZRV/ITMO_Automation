from pages.links_page import  Links

def test_home_link(browser):
    page_links = Links(browser)
    page_links.visit()

    assert page_links.link_home.get_text() == "Home"
    assert page_links.link_home.get_dom_attribute("href") == "https://demoqa.com/"

    main_window = browser.current_window_handle
    page_links.link_home.click()

    handles = browser.window_handles
    assert len(handles) > 1

    browser.switch_to.window(handles[1])
    assert browser.current_url == "https://demoqa.com/"
    browser.close()

    browser.switch_to.window(main_window)