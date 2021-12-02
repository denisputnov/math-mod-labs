import numpy as np

from draw_graphic import drawGraphic
from fibonacci import get_extremum_of_function_by_fibonacci_method
from golden_section import golden_section
from prettytable import PrettyTable

# func = lambda x: x / (1 + x**2)
# func = lambda x: np.sin(x)
# func = lambda x: 3 * x + 2 * np.sqrt(x)
func = lambda x: x**2 + 2*np.exp(x)


if __name__ == '__main__':
    a = int(input('Левая граница: '))
    b = int(input('Правая граница: '))
    eps = float(input('Точность: '))
    question = input('Задать количество итераций для фибоначи? [y/n]: ')
    if question == 'y':
        n = int(input('Количество итераций: '))
    else:
        n = None

    gss = golden_section(func, a, b, eps)
    fib = get_extremum_of_function_by_fibonacci_method(func, a, b, eps, n)

    t = PrettyTable(["Метод", "Минимум функции, X", "Значение функции", "Число итераций"])

    f, a, b = func, -5, 5
    func_values = []

    for x in np.linspace(a, b, 10000):
        func_values.append(f(x))

    t.add_row(["Золотое сечение", *gss])
    t.add_row(["Фибоначи", *fib])
    t.add_row(["Минимум", 0, round((min(func_values) + min(func_values) + 0.001) / 2, 4), 0])

    print(t)

    drawGraphic(a, b, func)