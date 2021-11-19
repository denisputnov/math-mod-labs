from utils import generate_random_variables, get_function_max
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

    return (b - a) / N * SUM
  

  @staticmethod
  def second(N):
    f, a, b = function()
    k = 0
    M = get_function_max(N)
    for _ in range(1, N + 1):
      X = a + (b - a) * random.random()
      Y = M * random.random()
      if Y < f(X):
        k += 1 

    I = M * (b - a) * k / N
    return I
