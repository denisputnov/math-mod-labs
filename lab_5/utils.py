import random
import numpy as np
from config import function


def generate_random_variables(x): 
  return [random.random() for _ in range(x)]


def get_function_max(linspaceLen):
  f, a, b = function()
  func_values = []
  for x in np.linspace(a, b, linspaceLen):
    func_values.append(f(x))
  
  return max(func_values)
  