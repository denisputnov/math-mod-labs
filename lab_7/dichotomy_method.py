from equations import *
import matplotlib.pyplot as plt


def dichotomy_method_with_param(eps, number, a, b, c, d, intervalA, intervalB):
    root = (intervalB + intervalA) / 2
    n = 0
    while intervalB - intervalA >= 2 * eps:
        n += 1
        if fun_with_param(a, b, c, d, root) == 0:
            break
        if fun_with_param(a, b, c, d, intervalA) * fun_with_param(a, b, c, d, root) < 0:
            intervalB = root
        elif fun_with_param(a, b, c, d, intervalB) * fun_with_param(a, b, c, d, root) < 0:
            intervalA = root
        root = (intervalB + intervalA) / 2
    print("Число итераций: ", n)
    print("С параметрами: ", round(root, number))
    plt.scatter(root, 0, color="red")


def dichotomy_method_without_param(eps, number, intervalA, intervalB):
    root = (intervalB + intervalA) / 2
    n = 0
    while intervalB - intervalA >= 2 * eps:
        n += 1
        if fun(root) == 0:
            break
        if fun(intervalA) * fun(root) < 0:
            intervalB = root
        elif fun(intervalB) * fun(root) < 0:
            intervalA = root
        root = (intervalB + intervalA) / 2
    print("Число итераций: ", n)
    print("Без параметров: ", round(root, number))
    plt.scatter(root, 0, color="green")
