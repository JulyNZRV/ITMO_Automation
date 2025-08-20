
# перейти на страницу https://demoqa.com/text-box
# ввести в первое поле произвольный текст
# подождать 2 сек
# очистить поле
# подождать 2 сек
# проверить, что в первом поле пусто


import time
from pages.text_box import TextBox


def test_clear(browser):
    tex_box = TextBox(browser)

    tex_box.visit()
    tex_box.name.send_keys("test")
    time.sleep(2)
    tex_box.name.clear()
    time.sleep(2)
    assert tex_box.name.get_text() == ""