import math
import numpy as np
import pandas as pd
import matplotlib.pyplot as plt
from requests import get
from PIL import Image


"""Библиотека math"""
print(math.comb(15, 4))  # количество сочетаний из 15 элементов по 4 без повторений без учета порядка
print(math.perm(15, 4))  # количество сочетаний из 15 элементов по 4 без повторений с учетом порядка
print(math.factorial(6))  # факториал
print(math.exp(4))  # значение экспоненциальной функции степени числа e

"""Библиотека numpy"""
a = np.array([9, 8, 7, 6])
b = np.array([1, 2, 3, 4])
print(a + b)
print(a - b)
print(a * b)
print(a / b)

"""Библиотека pandas"""
stud = pd.read_csv("Students_Performance_132b1e1ff9.csv")  # сторонний файл
print(stud.head(10))  # получение первых 10 строк
agg_functions = {"math score": ["mean", "median"]}
print(stud.groupby(["gender", "test preparation course"]).agg(agg_functions))

"""Библиотека matplotlib  визуализация данных. Изучение возможностей изображения данных в виде гистограммы"""
plt.hist(stud["math score"], label="Математический тест")
plt.xlabel("Баллы за тест")
plt.ylabel("К-во студентов")
plt.legend()
plt.show()

"""Библиотека requests"""
55.931491, 37.520076
response = get("https://static-maps.yandex.ru/1.x/?"
             "ll=37.520076,55.931491&"
             "spn=0.016457,0.00619&"
             "l=map")
print("Координаты студии профессиональной аквариумистики 'Неомарин'", response)
with open("map.png", "wb") as file:
    file.write(response.content)

"""Библиотека pillow"""
image = Image.open("162739.jpg")
image = image.resize((800, 600))
image.save("162739_1.jpg")
