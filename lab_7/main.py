# from simple_iteration_method import *
# from newton_method import *
# from dichotomy_method import *
# import matplotlib.pyplot as plt


# def create_plot(x, y1, y2, title):
#     plt.title(title)
#     plt.plot(x, y1)
#     plt.plot(x, y2)
#     plt.grid(True)
#     plt.show()


# # Вводим начальные значения
# a = float(input("Параметр a: "))
# b = float(input("Параметр b: "))

# x0 = float(input("Начальное приближение x: "))
# eps = float(input("Точность eps: "))

# # Узнаем количество знаков после запятой
# s = str(eps)
# number = abs(s.find('.') - len(s)) - 1

# n = int(input("Число итераций n: "))

# intervalA = float(input("Граница интервала A: "))
# intervalB = float(input("Граница интервала B: "))

# # Строим график функций для наглядности
# x = np.linspace(intervalA, intervalB, 1000)
# y1 = fun_with_param(a, b, c, d, x)
# # y2 = fun(x)

# print("\n-----------------------------------------------------------------")
# print("Метод простых итераций")

# # Ищем приближение для функции с параметрами
# iteration_method_with_param(x0, eps, number, a, b, c, d)
# # Ищем приближение для функции без параметрами
# iteration_method_without_param(x0, eps, number)

# # Показываем графики для метода простых итераций
# create_plot(x, y1, y2, "Метод простых итераций")

# print("-----------------------------------------------------------------")
# print("Метод Ньютона")

# # Ищем приближение для функции с параметрами
# newton_method_with_param(x0, n, a, b, c, d, eps, number)
# # Ищем приближение для функции без параметрами
# newton_method_without_param(x0, n, eps, number)

# # Показываем графики для метода Ньютона
# create_plot(x, y1, y2, "Метод Ньютона")

# print("-----------------------------------------------------------------")
# print("Метод дихотомии")

# # Ищем приближение для функции с параметрами
# dichotomy_method_with_param(eps, number, a, b, c, d, intervalA, intervalB)
# # Ищем приближение для функции без параметрами
# dichotomy_method_without_param(eps, number, intervalA, intervalB)

# # Показываем графики для метода дихотомии
# create_plot(x, y1, y2, "Метод дихотомии")
import numpy as np
from equations import *
import matplotlib.pyplot as plt

a = float(input('a: '))
b = float(input('b: '))

eps = 0.001
ROUND_TO = abs(str(eps).find('.') - len(str(eps))) - 1

start, end = float(input("start: ")), float(input("end: "))

x_values = np.linspace(start, end, int(1 / eps))
f1_y_values = [f1(a, x) for x in x_values]
f2_y_values = [f2(a, x) for x in x_values]

plt.plot(x_values, f1_y_values)
plt.plot(x_values, f2_y_values)
plt.grid(True)

plt.show()

x0 = float(input("Начальное приближениe: "))
n = int(input("Число итераций n: "))

def iterations(a, b, x): 
    if (np.abs(derivative_fi(a, b, x)) >= 1):
        exit("Итерации расходятся")
    prev = fi(a, b, x)

    print(prev)
    iterations = 0
    while np.abs(prev - x) >= eps:
        if (iterations >= n):
            exit("Цикл прерван из-за превышения лимита итераций.")
        if (np.abs(derivative_fi(a, b, x)) >= 1):
            exit("Итерации расходятся")
        iterations += 1
        x = np.abs(prev)
        prev = fi(a, b, x)

    print("Число итераций: ", iterations)
    print("С параметрами: ", round(prev, ROUND_TO))

iterations(a, b, x0)