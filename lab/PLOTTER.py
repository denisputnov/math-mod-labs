import matplotlib.pyplot as plt
import parser

import numpy as np
from scipy import interpolate

from inputs.filter_data import filter_data
from interpolation import Interpolation
from inputs.parse_interpolation_mode import parse_interpolation_mode
from approximation import approximation


class Plotter:
    def __init__(self, data_path) -> None:
        self.data = parser.parse_json_data(data_path)

    def _plot(self, x, y, label):
        plt.scatter(x, y, label=label)

    def _setting_and_show(self, title):
        plt.xlabel("Значение по X")
        plt.ylabel("Значение по Y")
        plt.title(title)
        plt.legend()
        plt.show()

    def plot_graph(self):
        for label, cords in filter_data(self.data).items():
            self._plot(cords['x'], cords['y'], label)
        self._setting_and_show("Простой поточечный график")

    def plot_interpolation(self):
        mode = parse_interpolation_mode()

        if mode == '1':
            self.draw_polynominal_interpolation()
        if mode == '2':
            self.draw_piecewise_linear_interpolation()
        if mode == '3':
            self.draw_piecewise_parabolic_interpolation()
        if mode == '4':
            self.draw_spline_interpolation()

    def draw_polynominal_interpolation(self):
        filtered_data = filter_data(self.data)
        for label, cords in filtered_data.items():
            xl = np.linspace(min(cords['x']), max(cords['x']))
            yl = Interpolation.polynomial_interpolation(cords['x'], cords['y'], xl)
            plt.scatter(cords['x'], cords['y'])
            plt.plot(xl, yl, label=label)
        self._setting_and_show("Промежуточные значения для данных, полученные посредством построения полинома Лагранжа")

    def draw_piecewise_linear_interpolation(self):
        filtered_data = filter_data(self.data)
        for label, cords in filtered_data.items():
            yl = [Interpolation.piecewise_linear_interpolation(cords['x'], cords['y'], value) for value in cords['x']]
            plt.scatter(cords['x'], cords['y'])
            plt.plot(cords['x'], yl, label=label)
        self._setting_and_show("Промежуточные значения для данных, полученные с использованием кусочно-линейного интерполирования")

    def draw_piecewise_parabolic_interpolation(self):
        filtered_data = filter_data(self.data)
        for label, cords in filtered_data.items():
            x_value = np.linspace(min(cords['x']), max(cords['x']), 1000)
            y_value = [Interpolation.piecewise_parabolic_interpolation(cords['x'], cords['y'], x) for x in x_value]
            plt.plot(x_value, y_value)
            plt.scatter(cords['x'], cords['y'], label=label)
        self._setting_and_show("Промежуточные значения для данных, полученные с использованием кусочно-параболического интерполирования")

    def draw_spline_interpolation(self):
        filtered_data = filter_data(self.data)
        for label, cords in filtered_data.items():
            xl = np.linspace(min(cords['x']), max(cords['x']))
            tck = interpolate.splrep(cords['x'], cords['y'], s=0)
            yl = interpolate.splev(xl, tck, der=0)
            plt.scatter(cords['x'], cords['y'])
            plt.plot(xl, yl, label=label)
        self._setting_and_show("Промежуточные значения для данных, полученные с использованием сплайн интерполирования")
    
    def plot_approximation(self):
        filtered_data = filter_data(self.data)
        power = int(input("Степень аппроксимирующего полинома: "))
        for label, cords in filtered_data.items():
            approximation(cords['x'], cords['y'], power)
            plt.scatter(cords['x'], cords['y'], label=label)
        self._setting_and_show("Задача аппроксимации")
