import numpy as np

def f1(a, x):
    return np.cos(a * x)

def f2(b, x):
    return -1 * b * np.log(x)

def fi(a, b, x):
    return np.cos(a * x) + b * np.log(x) + x

def derivative_fi(a, x, b):
    return b / x - a * np.sin(a * x) + 1

# Фунция с параметрами
def fun_with_param(a, b, x):
    return np.cos(a * x) + b * np.log(x)


def phi_with_param(a, b, x):
    return np.exp(-(np.cos(a * x) / b))


def derivative_fun_with_param(a, b, x):
    return b / x - a * np.sin(a * x)

def derivative_phi_with_param(a, b, x):
    return (a * np.sin(a * x) * np.exp(-np.cos(a * x) / b)) / b


# Функция без параметров
def fun(x):
    return x * (2 ** x) - 1


def phi(x):
    return 2 ** (-x)


def derivative_fun(x):
    return (2 ** x) * (1 + np.log(2) * x)


def derivative_phi(x):
    return -1 * np.log(2) / (2 ** x)
