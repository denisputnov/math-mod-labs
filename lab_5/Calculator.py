from scipy import integrate
from config import function

class Calculator:
  @staticmethod
  def analytically():
    f, a, b = function()
    return integrate.quad(f, a, b)[0] # аналитический интеграл по Ньютона-Лейбница

  @staticmethod
  def trapezium(n = 128): # n - число трапеций
    f, a, b = function()
    h = (b - a) / n # высота
    s = 0
    while round(a, 8) < b:
      s += 0.5 * h * (f(a) + f(a + h)) # считаем площадь
      a += h # сдвигаем левый край
    return s
