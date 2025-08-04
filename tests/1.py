def count_days(years, months):
    if years < 0 or months < 0:
        return

    total_days = (years * 12 + months) * 29
    print(total_days)

count_days(3, 3)  #3*12 + 3 = 1131
count_days(0, 5)  #5 * 29 = 145
count_days(5, 0)  #5*12 * 29 = 1740