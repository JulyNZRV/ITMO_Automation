class Soda:
    def __init__(self, ing=None):
        self.ing = ing

    def show_my_drink(self):
        if self.ing:
            print(f"Газировка и {self.ing}")
        else:
            print("Обычная газировка")


#Создаем объекты для тестирования
drink1 = Soda("малина")
drink2 = Soda()

#Вызываем метод для каждого объекта
drink1.show_my_drink()  # С добавкой
drink2.show_my_drink()  # Без добавки