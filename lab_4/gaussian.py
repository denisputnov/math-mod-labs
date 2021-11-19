from create_sampling import *
from graphs_points import create_histogram, create_polygon
from ploting import plot_histogram, plot_polygon
from math_utils import *
from sampling_value import *

def gaussian():
  m_gauss = float(input("Мат ожидание для распределения Гаусса: (M) "))
  d_gauss = float(input("Дисперсия для распределения Гаусса: (D) "))

  x_gauss, interval_gauss = create_gauss_sampling(m_gauss, d_gauss)
  data_hist_gauss, k_gauss = create_histogram(x_gauss, interval_gauss)
  data_polygon_gauss, _ = create_polygon(x_gauss, interval_gauss)

  plot_histogram(x_gauss, data_hist_gauss, k_gauss, interval_gauss, "Распределение Гаусса", 2, m=m_gauss, d=d_gauss)
  plot_polygon(x_gauss, data_polygon_gauss, interval_gauss, "Распределение Гаусса", 2, m=m_gauss, d=d_gauss)
  print("Мат ожидание распределения Гаусса: ", m_gauss)
  print("Дисперсия распределения Гаусса", d_gauss)

  mv = find_mathematical_expectation(x_gauss)

  print("Выборочное математическое ожидание распределения Гаусса:    ", mv)
  print("Выборочная дисперсия c известным МО распределения Гаусса:   ", find_dispersion(x_gauss, m_gauss))
  print("Выборочная дисперсия c неизвестным МО распределения Гаусса: ", find_dispersion(x_gauss, mv))
