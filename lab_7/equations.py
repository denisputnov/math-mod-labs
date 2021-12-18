import numpy as np

# 1 * (x**3) - 4 = 2 * (x**2) + 3 * x
# -(a * (x ** 3) + b * (x ** 2) + d) / c

def f1(a, d, x):
    return a * (x ** 3) + d

def f2(b, c, x):
    return - b * (x ** 2) - c * x

def f1_derivative(a, x):
    return 3 * a * (x ** 2)

def f2_derivative(b, c, x):
    return - 2 * b * x - c

def fi(a, b, c, d, x):
    return -(a * (x ** 3) + b * (x ** 2) + d) / c * 0.01

def fi_derivative(a, b, c, x):
    return (3 * a * x ** 2 + b * x) / c * 0.01

# def fi(a, b, c, d, x):
#     return f(a, b, c, d, x) * 0.01

# def fi_derivative(a, b, c, x):
#     return f_derivative(a, b, c, x)

# Фунция с параметрами
def fun_with_param(a, b, c, d, x):
    return a * (x**3) + b * (x**2) + c * x + d


def phi_with_param(a, b, c, d, x):
    return a * (x**3) + b * (x**2) + (c + 1) * x + d


def derivative_fun_with_param(a, b, c, x):
    return 3 * a * (x**2) + 2 * b * x + c


def derivative_phi_with_param(a, b, c, x):
    return 3 * a * (x**2) + 2 * b * x + c + 1


# Функция без параметров
def fun(x):
    return x * (2 ** x) - 1


def phi(x):
    return 2 ** (-x)


def derivative_fun(x):
    return (2 ** x) * (1 + np.log(2) * x)


def derivative_phi(x):
    return -1 * np.log(2) / (2 ** x)
