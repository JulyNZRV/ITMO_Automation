from pages.text_box import TextBox


def test_placeholder(browser):
    tex_box_page = TextBox(browser)
    tex_box_page.visit()
    assert tex_box_page.name.get_dom_attribute("placeholder") == "Full Name"