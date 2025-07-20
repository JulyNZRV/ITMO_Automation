#a: int = 5
#b: str = 'строка'
#с: list = [1, 2]

#def indent(s: str, width: int) -> str:
    #return " " * (max(0, width - len(s))) + s


#print(indent('134', 134))


#Задача_1
#создаем функцию
def task_1(a: int, b: float,c: str, d: list, e: bool) -> None:
    return a, b, c, d, e

#Создаем 5 переменных с разными типами:
a: int = 23
b: float = 3.14
c: str = "строка"
d: list = [1, 2, 3, 4, 5, "Я иду тебя искать"]
e: bool = True

#Выводим типы данных каждой переменной:
print(type(a), type(b), type(c), type(d), type(e))

#вызов функции
task_1(a, b, c, d, e)

#Задача_2
#создаем функцию
def task_2(a) -> int:
    return a

a = [1, 2, 3, 5, 8, 13, 21]

#Выводим в консоль первые3 значения списка:
print(1, 2, 3)

#вызов функции
task_2(a)

#d.Последовательность данных называется СПИСОК

#Задача_3
def task_3(a: int) -> int:
    return a ** 2

a: int = 3

print(task_3(a))