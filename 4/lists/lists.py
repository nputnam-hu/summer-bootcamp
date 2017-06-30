# define a function that takes in a list of postitive ints and returns its max element
def get_max(lst):
  max = -1
  for el in lst:
    if el >= max:
      max = el

  return max

# define a function that returns the sum of all elements of a list
def sum_list(lst):
  sum = 0
  for el in lst:
    sum += el

  return sum

# define a function that takes in a list of lists and returns one list with all of their elements in it
def flatten(lst):
  final_lst = []
  for sub_lst in lst:
    final_lst = final_lst + sub_lst

  return final_lst

# define a function to return the longest string of a list of strings
def longest_string(strings):
  largest_len = -1
  index = -1
  for i in range(len(strings)):
    if len(strings[i]) > largest_len:
      largest_len = len(strings[i])
      index = i

  return strings[index]
