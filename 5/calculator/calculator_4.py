import math
import bootcamp

class Calculator: 
  def __init__(self, n, use_degrees):
    self.n = n
    self.use_degrees = use_degrees
    # define list of valid operations to keep track of everything
    self.valid_operations = ["add", "add_n", "subtract", "multiply", "divide", "cos", "sin"]
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
    if self.use_degrees:
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

# note helper function that gets int from user
def get_input(num_inputs):
  inputs = []
  for i in range(num_inputs):
    inputs.append(bootcamp.get_int())

def main():
  print("~~~~Welcome to pycalculator~~~~")
  n = bootcamp.get_int("what is n?")
  use_degrees = False
  while True:
    choice = input("use degrees (y/n)?")
    if choice == "y":
      use_degrees = True
    elif choice == "n":
      use_degrees = False
  calculator = Calculator(n, use_degrees)

  while True:
    operation = intput("what operation? (type help for help, quit to exit")
    if operation == "quit":
      # quit program
      return
    if operation == "help":
      print("Avaliable Commands: ")
      for operation in calculator.valid_operations:
        print(operation)
    if operation in calculator.valid_operations:

      args = get_input(2)
      print(calculator.operation(*args) # same as print(calculator.add(args[0], args[1]))
    else:
      print("INVALID OPERATION")


if __name__ == "__main__":
  main()
