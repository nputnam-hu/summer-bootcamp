# extend to use functions, also prints out numbers at top

nums = [1,2,3,4,5,6,7,8,9,10]

def main():
  # print some space out
  print("     ", end="")
  for i in nums:
    print(" %2i " % (i), end="")
  enter()
  print("     ", end="")
  # print row underneath to seperate
  for i in nums:
    print (" __ ", end ="")
  enter()
  for i in nums:
    # print number on left
    print(" %2i| " % (i), end = "")
    for j in nums:
      # print multiplacations
      print(" %2i " % (i*j), end = "")
    enter()

# mimicks enter key
def enter():
  print("\n", end="")


if __name__ == "__main__":
  main()
