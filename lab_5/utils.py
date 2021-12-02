import random
import numpy as np
from scipy import integrate
from config import function


def generate_random_variables(x): 
  return [random.random() for _ in range(x)]


def get_max_min():
  f, a, b = function()
  func_values = []
  for x in np.linspace(a, b, 10000):
    func_values.append(f(x))

  return max(func_values), min(func_values)
  
def math_expectation():
  pass
