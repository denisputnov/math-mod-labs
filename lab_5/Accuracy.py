import numpy as np
from Calculator import Calculator


class Accuracy:
  @staticmethod
  def trapezium(n):
    return Calculator.trapezium(2*n) - Calculator.trapezium(n)
    
  @staticmethod
  def one_percent(func):
    expect = np.abs(Calculator.analytically()) # ожидаемый процент точности
    accuracy = 100 # изначальный процент
    n = 1 # количество узлов 
    prev = np.abs(func(n)) # значение функции
    while accuracy > 1: # итерабельно проходим пока не достигнем ожидаемой точности
      n *= 2
      now = np.abs(func(n))
      accuracy = np.abs((now - prev) * 100 / expect)
      prev = now

    return n
