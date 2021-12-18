from equations import *
import matplotlib.pyplot as plt


def iteration_method_with_param(x, eps, number, a, b, c, d, iterations):
    if abs(fi_derivative(a, b, c, x)) >= 1:
        exit(f"Итерационный процесс расходится {fi_derivative(a,b,c,-2)}")
    print(fi_derivative(a,b,c,x))
    root = fi(a, b, c, d, x)
    n = 0
    while abs(root - x) >= eps and n < iterations:
        print(n)
        n += 1
        x = root
        root = fi(a, b, c, d, x)
    print("Число итераций: ", n)
    print("X: ", round(root, number))
    plt.scatter(root, 0, color="red")


def iteration_method_without_param(x, eps, number):
    root = phi(x)
    n = 0
    while abs(root - x) >= eps:
        n += 1
        x = root
        root = phi(x)
    print("Число итераций: ", n)
    print("X: ", round(root, number))
    y = f2(2,3, x) 
    plt.scatter(root, y, color="green")
