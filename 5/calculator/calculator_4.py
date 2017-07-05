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
    if self.use_degrees:
      # convert to radians
      x = math.radians(x)
    # round to the 5th decimal place
    return round(math.sin(x), 5)

# note helper function that gets int from user
def get_input(num_inputs):
  inputs = []
  for i in range(num_inputs):
    inputs.append(bootcamp.get_int("value?"))
  return inputs

def main():
  print("~~~~Welcome to pycalculator~~~~")
  n = bootcamp.get_int("what is n?")
  use_degrees = False
  while True:
    choice = input("use degrees (y/n)? ")
    if choice == "y":
      use_degrees = True
      break
    elif choice == "n":
      use_degrees = False
      break
  calculator = Calculator(n, use_degrees)

  while True:
    operation = input("what operation? (type help for help, quit to exit) ")
    if operation == "quit":
      # quit program
      return

    if operation == "help":
      print("Avaliable Commands: ")
      for op in calculator.valid_operations:
        print(op)

    elif operation in calculator.valid_operations:
      if operation == "add":
        args = get_input(2)
        print(calculator.add(*args)) # same as print(calculator.add(args[0], args[1]))
      if operation == "add_n":
        args = get_input(1)
        print(calculator.add_n(*args))
      if operation == "subtract":
        args = get_input(2)
        print(calculator.subtract(*args))
      if operation == "multiply":
        args = get_input(2)
        print(calculator.multiply(*args))
      if operation == "divide":
        args = get_input(2)
        print(calculator.multiply(*args))
      if operation == "cos":
        args = get_input(1)
        print(calculator.cos(*args))
      if operation == "sin":
        args = get_input(1)
        print(calculator.sin(*args))
    else:
      print("INVALID INPUT")



if __name__ == "__main__":
  main()
