# consolodate seperate method into init
class Employee:
  def __init__(self, name):
    self.name = name
    self.nametag = "Hello, my name is " + name

alex = Employee("Alex")
print(alex.nametag) # Hello, my name is Alex