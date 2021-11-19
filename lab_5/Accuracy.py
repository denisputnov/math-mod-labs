import numpy as np
from Calculator import Calculator


class Accuracy:
  @staticmethod
  def trapezium(n):
    return Calculator.trapezium(2*n) - Calculator.trapezium(n)
    
  @staticmethod
  def one_percent(func):
    expect = np.abs(Calculator.analytically() / 100) # ожидаемый процент точности
    i = 100 # изначальный процент
    n = 1 # количество узлов 
    prev = func(n) # значение функции
    while i > expect: # итерабельно проходим пока не достигнем ожидаемой точности
      n *= 2
      trapezium = func(n)
      i = np.abs(trapezium - prev)
      prev = trapezium
    
    return n
