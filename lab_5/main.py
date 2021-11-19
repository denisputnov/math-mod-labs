from matplotlib import pyplot as plt
import numpy as np
from numpy import std
from prettytable import PrettyTable

from Accuracy import Accuracy
from Calculator import Calculator
from MonteKarlo import MonteKarlo
from config import NUMBER_OF_DIGITS_AFTER_DOT, function


def plot():
  f, a, b = function()
  x = np.linspace(a, b, 100)
  plt.plot(x, f(x))

  plt.xlabel('x')
  plt.ylabel('y')
  plt.show()
    

if __name__ == '__main__':
  plot()

  trapezium = Accuracy.one_percent(Calculator.trapezium)
  first = Accuracy.one_percent(MonteKarlo.first)
  second = Accuracy.one_percent(MonteKarlo.second)

  t = PrettyTable(["Параметр", "Значение"])
  t2 = PrettyTable(["Метод", "Количество узлов для точности в 1%"])

  t.add_row(["Аналитическйи способ ", round(Calculator.analytically(), NUMBER_OF_DIGITS_AFTER_DOT)])
  t.add_row(["Метод трапеций", round(Calculator.trapezium(trapezium), NUMBER_OF_DIGITS_AFTER_DOT)])
  t.add_row(["Оценка интеграла по первому методу М-К", round(MonteKarlo.first(first), NUMBER_OF_DIGITS_AFTER_DOT)])
  t.add_row(["Оценка интеграла по второму методу М-К", round(MonteKarlo.second(second), NUMBER_OF_DIGITS_AFTER_DOT)])
  t.add_row(["Стандартное отклонение для 1 метода М-К", round(std([MonteKarlo.first(first)  for _ in range(100)]), NUMBER_OF_DIGITS_AFTER_DOT)])
  t.add_row(["Стандартное отклонение для 2 метода М-К", round(std([MonteKarlo.second(second)  for _ in range(100)]), NUMBER_OF_DIGITS_AFTER_DOT)])

  t2.add_row(["Метод трапеций", trapezium])
  t2.add_row(["Первый способ М-К", first])
  t2.add_row(["Второй способ М-К", second])

  print(t2)
  print(t)