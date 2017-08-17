import bootcamp

height = -1
while True: 
  height = bootcamp.get_int("height? ")
  if height > 0 and height <= 23:
      break
 
for i in range(height):
    for space in range(height - i - 1):
        print(" ", end="")
    for hashes in range(2 + i):
        print("#", end="")
    print("\n", end="")

