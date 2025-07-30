#1. Создайте функцию которая
#a. переходит на страницу https://www.saucedemo.com/
#b. находит элементы:
#i. текстовое поле username
#ii. текстовое поле password
#iii. кнопку submit

# from selenium import webdriver
# from selenium.webdriver.common.by import By
#
# driver = webdriver.Chrome()
# driver.get("https://www.saucedemo.com/")
#
# # b. Поиск элементов:
# username = driver.find_element(By.ID, "user-name")  # i. текстовое поле username
# password = driver.find_element(By.ID, "password")  # ii. текстовое поле password
# submit = driver.find_element(By.ID, "login-button")  # iii. кнопка submit
#
# print("Элементы найдены")


from selenium import webdriver
from selenium.webdriver.common.by import By

driver = webdriver.Chrome()
driver.get("https://www.saucedemo.com/")

username = driver.find_elements(By.ID, "user-name")  # возвращает список элементов
password = driver.find_elements(By.ID, "password")
submit = driver.find_elements(By.ID, "login-button")

if username and password and submit:
    print("Элементы найдены")
else:
    print("Не все элементы найдены")


