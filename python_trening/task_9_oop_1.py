# Импортируем базовый класс из другого файла
from task_9_checks import Checks

# Создаём дочерние классы, наследующие от Checks
class Input(Checks):
    def __init__(self, loc, text):
        super().__init__(loc)  # Инициализируем родительский класс?
        self.text = text

class Button(Checks):
    def __init__(self, loc, text):
        super().__init__(loc)
        self.text = text

class Title(Checks):
    def __init__(self, loc, text):
        super().__init__(loc)
        self.text = text

class Link(Checks):
    def __init__(self, loc, text):
        super().__init__(loc)
        self.text = text

# Создаём объекты
input_obj = Input("input#search", "Поле поиска")
button_obj = Button("button#submit", "Отправить")
title_obj = Title("h1.title", "Главная страница")
link_obj = Link("a.home", "Домой")

# Вызываем метод check_text() для каждого объекта
print(input_obj.check_text())
print(button_obj.check_text())
print(title_obj.check_text())
print(link_obj.check_text())