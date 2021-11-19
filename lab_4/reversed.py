from create_sampling import *
from graphs_points import create_histogram, create_polygon
from ploting import plot_histogram, plot_polygon
from math_utils import *
from sampling_value import *

def reversed_functions():
  a = int(input("a: "))
  b = int(input("b: "))

  x_normal, interval_normal = create_normal_sampling(a, b)
  data_hist_normal, k_normal = create_histogram(x_normal, interval_normal)
  data_polygon_normal, _ = create_polygon(x_normal, interval_normal)

  plot_histogram(x_normal, data_hist_normal, k_normal, interval_normal, "Равномерное распределение (гистограма)", 1)
  plot_polygon(x_normal, data_polygon_normal, interval_normal, "Равномерное распределение (полигоны)", 1)

  print("Мат ожидание: ", (b + a) / 2)
  print("Дисперсия", (b - a) ** 2 / 12)

  mn = find_mathematical_expectation(x_normal)
  # Для равномерных распределений
  print("Выборочное математическое ожидание равномерного распределения:    ", mn)
  print("Выборочная дисперсия равномерного распределения c известным МО:   ", find_dispersion(x_normal, (b + a) / 2))
  print("Выборочная дисперсия равномерного распределения c неизвестным МО: ", find_dispersion(x_normal, mn))
