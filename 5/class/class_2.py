
class Hello:
  def define_hello(self):
    self.hello_value = "hello, world"
  def hello(self):
    print(self.hello_value)

instanstiation = Hello()
instanstiation.define_hello()
instanstiation.hello() # prints hello, world
