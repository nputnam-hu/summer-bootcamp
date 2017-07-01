
file = open("sample.txt")
for line in file:
  # remove \n char
  line = line.strip()
  if line == "hello" or line == "world":
    print(line)


nums = [1,2,3,4]
x = bootcamp.get_int("x?")
if x in nums:
  print(x)