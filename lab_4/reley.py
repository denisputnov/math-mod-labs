from create_sampling import *
from graphs_points import create_histogram, create_polygon
from ploting import plot_histogram, plot_polygon
from math_utils import *
from sampling_value import *
import math
from prettytable import PrettyTable

def reley():
  sigma_rayleigh = float(input("Sigma: "))

  x_neumann, interval_neumann = create_rayleigh_sampling(sigma_rayleigh)
  data_hist_neumann, k_neumann = create_histogram(x_neumann, interval_neumann)
  data_polygon_neumann, _ = create_polygon(x_neumann, interval_neumann)

  plot_histogram(
    x_neumann, 
    data_hist_neumann, 
    k_neumann, 
    interval_neumann, 
    "Плотность вероятности распределения Реле (гистограма)", 
    3,
    sigma=sigma_rayleigh
  )
  plot_polygon(
    x_neumann, 
    data_polygon_neumann, 
    interval_neumann, 
    "Функция распределения распределения Реле (полигоны)", 
    3,
    sigma=sigma_rayleigh
  )

  m_ne = math.sqrt((math.pi * (sigma_rayleigh ** 2)) / 2) # мат ожидание рраспределения Рэле
  mk = find_mathematical_expectation(x_neumann)

  t = PrettyTable([
    "Величина",
    "Значение"
  ])

  t.add_row(['Математическое ожидание распрееделение Рэле', m_ne])
  t.add_row(['Дисперсия распределения Рэле', (2 - math.pi / 2) * (sigma_rayleigh ** 2)])
  t.add_row(['Выборочное математическое ожидание распределения Рэле', mk])
  t.add_row(['Выборочная дисперсия распределения Рэле с известным МО', find_dispersion(x_neumann, m_ne)])
  t.add_row(['Выборочная дисперсия распределения Рэле с неизвестным МО', find_dispersion(x_neumann, mk)])

  print(t)
