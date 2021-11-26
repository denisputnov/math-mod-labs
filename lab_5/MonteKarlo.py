import numpy as np
from utils import generate_random_variables, get_max_min
import random
from config import function

class MonteKarlo: 
  @staticmethod
  def first(N = 100):
    f, a, b = function()
    SUM = 0
    random_values = generate_random_variables(N)
    for i in range(N):
      U =  random_values[i] * (b - a) + a
      SUM += f(U)

    return np.abs((b - a) / N * SUM)
  

  @staticmethod
  def second(N):
    f, a, b = function()
    k = 0
    max, min = get_max_min()
    for _ in range(N):
      X = random.uniform(a, b)
      Y = random.uniform(max, min)
      if Y > f(X):
        k += 1 

    I = (max - min) * np.abs(b - a) * k / N
    return I
