import numpy as np
from Calculator import Calculator


class Accuracy:
  @staticmethod
  def trapezium(n):
    return Calculator.trapezium(2*n) - Calculator.trapezium(n)
    
  @staticmethod
  def one_percent(func):
    expect = np.abs(Calculator.analytically()) # ожидаемый процент точности
    i = 100 # изначальный процент
    n = 1 # количество узлов 
    prev = np.abs(func(n)) # значение функции
    while i > expect: # итерабельно проходим пока не достигнем ожидаемой точности
      n *= 2
      now = np.abs(func(n))
      i = np.abs((now - prev) * 100 / prev)
      prev = now

    return n
