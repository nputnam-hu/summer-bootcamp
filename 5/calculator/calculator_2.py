class Calculator:
  def __init__(self, n):
    self.n = n
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

def main():
  calculator = Calculator(5)
  print(calculator.add(1,2))
  print(calculator.subtract(5,3))
  print(calculator.multiply(2,10))
  print(calculator.divide(10, 5))
  print(calculator.add_n(10))

if __name__ == "__main__":
  main()
