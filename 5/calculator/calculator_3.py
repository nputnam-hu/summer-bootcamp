import math

class Calculator: 
  def __init__(self, n, useDegrees):
    self.n = n
    self.useDegrees = useDegrees
  def add(self, x, y):
    return x + y
  def add_n(self, x):
    return x + self.n
  def subtract(self, x, y):
    return x - y
  def multiply(self, x, y):
    return x * y
  def divide(self, x, y):
    return x / y
  def cos(self, x):
    if self.useDegrees:
      # convert to radians
      x = math.radians(x)
    # round to the 5th decimal place
    return round(math.cos(x), 5)

  def sin(self, x):
    if self.useDegrees:
      # convert to radians
      x = math.radians(x)
    # round to the 5th decimal place
    return round(math.sin(x), 5)


def main():
  calculator = Calculator(5, True)
  print(calculator.cos(90))

if __name__ == "__main__":
  main()
