class Employee:
  def __init__(self, name):
    self.name = name
  def create_nametag(self):
    self.nametag = "Hello, my name is " + self.name

alex = Employee("Alex")
alex.create_nametag()
print(alex.nametag) # Hello, my name is Alex