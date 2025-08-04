#task2
def print_max(a, b):
    if a > b:
        print(a)
    else:
        print(b)

print_max(7, 9)


#task3
def difference(a, b):
    if abs(a - b) == 135:
        print("yes")
    else:
        print("no")

difference(1, 136)
difference(1, 5)


#task4
def season(month):
    if month in [12, 1, 2]:
        print('зима')
    elif month in [3, 4, 5]:
        print('весна')
    elif month in [6, 7, 8]:
        print('лето')
    elif month in [9, 10, 11]:
        print('осень')
    else:
        print('введите число от 1 до 12')

season(1)
season(4)
season(7)
season(10)
season(14)


#task5
def get_numbers(a, b, c):
    if a > 10 and b > 10 and c > 10:
        print("yes")
    else:
        print("no")

get_numbers(17, 12, 25)
get_numbers(17, 12, 7)
get_numbers(17, 5, 25)
get_numbers(10, 12, 25)

#Доп*
#task6
def count_positive(numbers):
    positive_count = sum(1 for num in numbers if num > 0)
    print(positive_count)

count_positive([-1, -2, -3, -4, 0])
count_positive([-1, -2, -3, -4, 1])
count_positive([-1, -2, 0, 4, 1])
count_positive([-1, -2, 3, 4, 1])


#task7
def count_days(years, months):
    if years < 0 or months < 0:
        return

    total_days = (years * 12 + months) * 29
    print(total_days)

count_days(3, 3)  #3 * 12 + 3 = 1131
count_days(0, 5)  #5 * 29 = 145
count_days(5, 0)  #5 * 12 * 29 = 1740





