from create_sampling import *
from graphs_points import create_histogram, create_polygon
from ploting import plot_histogram, plot_polygon
from math_utils import *
from sampling_value import *
from prettytable import PrettyTable

def reversed_functions():
  a = int(input("a: "))
  b = int(input("b: "))

  x_normal, interval_normal = create_normal_sampling(a, b)
  data_hist_normal, k_normal = create_histogram(x_normal, interval_normal)
  data_polygon_normal, _ = create_polygon(x_normal, interval_normal)

  plot_histogram(
    x_normal, 
    data_hist_normal, 
    k_normal, 
    interval_normal, 
    "Плотность вероятности равномерного распределения (гистограма)", 
    1
  )
  plot_polygon(
    x_normal, 
    data_polygon_normal, 
    interval_normal, 
    "Функция распределения равномерного распределения (полигоны)", 
    1
  )

  mn = find_mathematical_expectation(x_normal)

  t = PrettyTable([
    "Величина",
    "Значение"
  ])

  t.add_row(['Мат ожидание', (b + a) / 2])
  t.add_row(['Дисперсия', (b - a) ** 2 / 12])
  t.add_row(['Выборочное математическое ожидание равномерного распределения', round(mn, 3)])
  t.add_row(['Выборочная дисперсия равномерного распределения c известным МО', round(find_dispersion(x_normal, (b + a) / 2), 3)])
  t.add_row(['Выборочная дисперсия равномерного распределения c неизвестным МО', round(find_dispersion(x_normal, mn), 3)])

  print(t)