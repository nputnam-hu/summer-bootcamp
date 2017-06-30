# extend to use functions, also prints out numbers at top
import bootcamp

def main():
  num = -1
  # restrict to max of 3 digits
  while num < 0 or num > 30:
    num = bootcamp.get_int("n?")
  table(num)

def table(n):
  print("      ", end="")
  for i in range(1,n+1):
    print(" %3i " % (i), end="")
  enter()
  print("      ", end="")
  for i in range(1,n+1):
    print (" ___ ", end ="")
  enter()
  for i in range(1,n+1):
    print(" %3i| " % (i), end = "")
    for j in range(1,n+1):
      print(" %3i " % (i*j), end = "")
    enter()

# mimicks enter key
def enter():
  print("\n", end="")


if __name__ == "__main__":
  main()