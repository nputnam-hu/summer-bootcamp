import bootcamp

minutes = -1
while True:
  minutes = bootcamp.get_int("Minutes?")
  if minutes >= 0:
    break
  else:
    print("invalid minutes, try again")

bottles = minutes * 12
print("That shower was equivalent to %i bottles of water" % (bottles))

