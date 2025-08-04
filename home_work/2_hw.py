#task_1
def task_1() -> tuple[type, type, type, type, type]:
     # Создаем переменные внутри функции
        a: int = 42
        b: float = 3.14
        c: str = "строка"
        d: list = [1, 2, 3, 4, 5, 'Я иду тебя искать']
        e: bool = True

# Выводим типы данных каждой в консоль (внутри функции)
        print(type(a), type(b), type(c), type(d), type(e))
        return type(a),type(b), type(c),type(d),type(e)

# Вызов функции
task_1()


#Задача_2
def task_2() -> None:
     a = [1, 2, 3, 5, 8, 13, 21]
     print(a[:3]) # Выводим первые 3 значения списка внутри функции

#вызов функции
task_2()

#d.Последовательность данных называется числа Фибоначчи

#Задача_3
def task_3(a: int) -> None:
    return a ** 2

a: int = 3

print(task_3(a))