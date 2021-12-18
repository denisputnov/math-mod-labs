from equations import *
import matplotlib.pyplot as plt


def newton_method_with_param(x, n, a, b, c, d, eps, number):
    root = x
    # число итерций
    N = 0
    for i in range(n):
        N += 1
        root = x - (f(a, b, c, d, x) / f_derivative(a, b, c, x))
        # Если разница между текущим корнем и предыдущим меньше eps
        if abs(root - x) < eps:
            break
        x = root
    print("Итераций: ", N)
    print("X: ", round(root, number))
    y = f(a,b,c,d,x)
    plt.scatter(root, y, color="red")


def newton_method_without_param(x, n, eps, number):
    root = x
    # число итерций
    N = 0
    for i in range(n):
        N += 1
        root = x - (fun(x) / derivative_fun(x))
        # Если разница между текущим корнем и предыдущим меньше eps
        if abs(root - x) < eps:
            break
        x = root
    print("Число итераций: ", N)
    print("Без параметров: ", round(root, number))
    plt.scatter(root, 0, color="green")
