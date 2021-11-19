NUMBER_OF_DIGITS_AFTER_DOT = 8


def function():
  # return lambda x: np.log(x) / x, 0.5, 5
  # return lambda x: np.sin(x) / (1 + np.cos(x)), 2, 3
  return lambda x: x / (1 + x**2), -4, 0
