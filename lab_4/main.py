from gaussian import gaussian
from reley import reley
from reversed import reversed_functions

def main():
  print("1 - Выборка случайных величин методом обратных функций")
  print("2 - Выборка величин, распредленных по Гауссовскому закону с математическим ожиданием и дисперсией")
  print("3 - Выборка случайных значенй по методу Неймана")

  option = input()
  if (option == '1'):
    reversed_functions()
  if (option == '2'):
    gaussian()
  if (option == '3'):
    reley()

if __name__ == "__main__":
  main()
