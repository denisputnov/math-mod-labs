from math_utils import *
from quicksort import quicksort
import random


def create_normal_sampling(a, b):
    if a > b:
        print("Неверные данные")
        raise SystemExit(1)
    r = generate_random_variables(1000)
    x = []
    for i in r:
        xr = reverse_fun(i, a, b)
        x.append(xr)
    x = quicksort(x)
    interval = [a, b]
    return x, interval


def create_gauss_sampling(m, d):
    sigma = math.sqrt(d)
    n = 6
    x = []
    for _ in range(1000):
        v = 0
        for _ in range(n):
            v += random.random()
        xi = fun_gauss(v, m, sigma, n)
        x.append(xi)
    x = quicksort(x)
    interval = [x[0], x[-1]]
    return x, interval


def create_rayleigh_sampling(sigma):
    # Максимальное значение приобретает функция если аргумент xl равен sigma
    max_y = rayleigh_distribution(sigma, sigma)
    ri = generate_random_variables(5000)
    x = []
    for i in range(5000):
        X = 4 * sigma * ri[i]
        Y = max_y * ri[i - 1]
        if Y <= rayleigh_distribution(X, sigma):
            x.append(X)
        if len(x) >= 1000:
            break
    x = quicksort(x)
    interval = [0, x[-1]]
    return x, interval
