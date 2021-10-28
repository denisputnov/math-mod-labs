import numpy as np
import matplotlib.pyplot as plt

def approximation(x, y, power):
    polynom = np.polyfit(x, y, power) # получает полином по методу наименьших квадратов
    polynom_function = np.poly1d(polynom)
    x_values = np.linspace(np.min(x), np.max(x))
    y_values = polynom_function(x_values)
    plt.plot(x_values, y_values)
