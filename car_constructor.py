class Car:
    def __init__(self, color, type, year):
        self.color = color
        self.type = type
        self.year = year

    def start_engine(self):
        print('Автомобиль заведен')

    def stop_engine(self):
        print('Автомобиль заглушен')

    def set_year(self, new_year):
        self.year = new_year
        print(f'Год выпуска: {self.year}')

    def set_type(self, new_type):
        self.type = new_type
        print(f'Тип автомобиля: {self.type}')

    def set_color(self, new_color):
        self.color = new_color
        print(f'Цвет автомобиля: {self.color}')


#Создаем объект автомобиля
my_car = Car('Черный', 'Седан', 2020)


my_car.start_engine()
my_car.set_year(2022)
my_car.set_type('Хэтчбек')
my_car.set_color('Синий')
my_car.stop_engine()

