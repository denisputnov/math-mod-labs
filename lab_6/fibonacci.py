from math import sqrt
from typing import Union


def fibonacci(n):
    return (pow((1 + sqrt(5)) / 2, n + 1) - pow((1 - sqrt(5)) / 2, n + 1)) / sqrt(5)


def get_iterations_quantity(a, b, eps):
    k = (b - a) / eps
    n = 0
    while fibonacci(n) <= k:
        n += 1

    return n


def fibonacci_method(function, a, b, x1, x2, n):
    if n == 1:
        return (x1 + x2) / 2

    if function(x1) > function(x2):
        a = x1
        x1 = x2
        x2 = b - x1 + a
    else:
        b = x2
        x2 = x1
        x1 = a + b - x2

    return fibonacci_method(function, a, b, x1, x2, n - 1)


def get_extremum_of_function_by_fibonacci_method(function, a, b, eps, n=None):
    if not n:
        n = get_iterations_quantity(a, b, eps)
    x1 = a + (b - a) * fibonacci(n - 2) / fibonacci(n)
    x2 = a + (b - a) * fibonacci(n - 1) / fibonacci(n)

    return round(fibonacci_method(function, a, b, x1, x2, n), 3), round(function(
        fibonacci_method(function, a, b, x1, x2, n)), 3), f'Итераций: {n}'