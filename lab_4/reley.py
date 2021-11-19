from create_sampling import *
from graphs_points import create_histogram, create_polygon
from ploting import plot_histogram, plot_polygon
from math_utils import *
from sampling_value import *
import math

def reley():
  sigma_rayleigh = float(input("Введите сигму для релеевского закона: "))
  print("\n\n\n")

  x_neumann, interval_neumann = create_rayleigh_sampling(sigma_rayleigh, 4)
  data_hist_neumann, k_neumann = create_histogram(x_neumann, interval_neumann)
  data_polygon_neumann, _ = create_polygon(x_neumann, interval_neumann)

  plot_histogram(x_neumann, data_hist_neumann, k_neumann, interval_neumann, "Распределение Реле", 3,
                sigma=sigma_rayleigh)
  plot_polygon(x_neumann, data_polygon_neumann, interval_neumann, "Распределение Реле", 3,
              sigma=sigma_rayleigh)


  m_ne = math.sqrt((math.pi * (sigma_rayleigh ** 2)) / 2)
  print("Математическое ожидание распрееделение Рэле ", m_ne)
  print("Дисперсия распределения Рэле: ", (2 - math.pi / 2) * (sigma_rayleigh ** 2))
  mk = find_mathematical_expectation(x_neumann)
  print("Выборочное математическое ожидание распределения Рэле:    ", mk)
  print("Выборочная дисперсия распределения Рэле с известным МО:   ", find_dispersion(x_neumann, m_ne))
  print("Выборочная дисперсия распределения Рэле с неизвестным МО: ", find_dispersion(x_neumann, mk))
