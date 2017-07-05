class Calculator:
  def __init__(self):
    return
  def add(self, x, y):
    return x + y
  def subtract(self, x, y):
    return x - y
  def multiply(self, x, y):
    return x * y
  def divide(self, x, y):
    return x / y

def main():
  calculator = Calculator()
  print(calculator.add(1,2))
  print(calculator.subtract(5,3))
  print(calculator.multiply(2,10))
  print(calculator.divide(10, 5))

if __name__ == "__main__":
  main()
