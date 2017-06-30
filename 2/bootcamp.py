# helper functions

def get_int(question):
  x = -1
  while 1: 
    try:
     x = int(raw_input(question + " "))
     break
    except:
      pass 
  return x