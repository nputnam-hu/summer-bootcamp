# helper functions

def get_int(question):
  x = -1
  while 1: 
    try:
     x = int(input(question + " "))
     break
    except ValueError:
      pass 
  return x
