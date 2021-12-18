from equations import *
import matplotlib.pyplot as plt


def iteration_method_with_param(x, eps, number, a, b, c, d):
    if abs(derivative_phi_with_param(a, b, c, x)) >= 1:
        return print("Итерационный процесс расходится")
    root = phi_with_param(a, b, c, d, x)
    n = 0
    while abs(root - x) >= eps:
        if abs(derivative_phi_with_param(a, b, c, root)) >= 1:
            return print("Итерационный процесс расходится")
        n += 1
        x = root
        root = phi_with_param(a, b, c, d, x)
    print("Число итераций: ", n)
    print("С параметрами: ", round(root, number))
    plt.scatter(root, 0, color="red")


def iteration_method_without_param(x, eps, number):
    root = phi(x)
    n = 0
    while abs(root - x) >= eps:
        n += 1
        x = root
        root = phi(x)
    print("Число итераций: ", n)
    print("Без параметров: ", round(root, number))
    plt.scatter(root, 0, color="green")
