#task1 создайте класс прямоугольника
class Rectangle:
    def __init__(self, width, height):
        self.width = width
        self.height = height

    def calculate_area(self):
        return self.width * self.height

    def calculate_perimeter(self):
        return 2 * (self.width + self.height)


# Создаем три прямоугольника
rect1 = Rectangle(7, 11)
rect2 = Rectangle(3, 7)
rect3 = Rectangle(8, 4)

# Рассчитываем и выводим площадь и периметр каждого
print(f'Прямоугольник 1: ширина={rect1.width}, высота={rect1.height}')
print(f'  Площадь: {rect1.calculate_area()}')
print(f'  Периметр: {rect1.calculate_perimeter()}\n')

print(f'Прямоугольник 2: ширина={rect2.width}, высота={rect2.height}')
print(f'  Площадь: {rect2.calculate_area()}')
print(f'  Периметр: {rect2.calculate_perimeter()}\n')

print(f'Прямоугольник 3: ширина={rect3.width}, высота={rect3.height}')
print(f'  Площадь: {rect3.calculate_area()}')
print(f'  Периметр: {rect3.calculate_perimeter()}')


#task2 cоздайте класс Math
class Math:
    def __init__(self, a, b):
        self.a = a
        self.b = b

    def addition(self):
        """Сложение a и b"""
        result = self.a + self.b
        print(f'Сложение: {self.a} + {self.b} = {result}')
        return result

    def multiplication(self):
        """Умножение a и b"""
        result = self.a * self.b
        print(f'Умножение: {self.a} × {self.b} = {result}')
        return result

    def division(self):
        """Деление a на b"""
        if self.b == 0:
            print('Ошибка: деление на ноль невозможно!')
            return None
        result = self.a / self.b
        print(f'Деление: {self.a} / {self.b} = {result}')
        return result

    def subtraction(self):
        """Вычитание b из a"""
        result = self.a - self.b
        print(f'Вычитание: {self.a} - {self.b} = {result}')
        return result


# Создаем объект Math
calculator = Math(10, 5)

# Выполняем операции
calculator.addition()
calculator.multiplication()
calculator.division()
calculator.subtraction()

# Тестируем деление на ноль
zero_div = Math(10, 0)
zero_div.division()


#task3
class SidebarButton:
    def __init__(self, text):
        self.text = text
        self.type = 'Кнопка'
        self.locator = ""  # По умолчанию пустая строка

    def click(self):
        return f'Клик по кнопке {self.text}'


# Список всех кнопок 2-го уровня из сайдбара
buttons_data = [
    'Text Box',
    'Check Box',
    'Radio Button',
    'Web Tables',
    'Buttons',
    'Links',
    'Broken Links - Images',
    'Upload and Download',
    'Dynamic Properties'
]

#Cоздаем объекты для каждой кнопки
sidebar_buttons = [SidebarButton(text) for text in buttons_data]

#Выводим текст для каждой кнопки
print('Тексты кнопок:')
for button in sidebar_buttons:
    print(f'- {button.text} ({button.type})')

print('\nКлик:')
#Вызываем метод click() для каждой кнопки
for button in sidebar_buttons:
    print(button.click())