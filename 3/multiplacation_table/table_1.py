nums = [1,2,3,4,5,6,7,8,9,10]

for i in nums:
  for j in range(10,20):
    nums[j]
    print(" %.2i " % (i*j), end = "")
  print("\n", "")