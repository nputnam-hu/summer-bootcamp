def main():
  count = 0
  file = open("content.txt")
  for line in file:
    for char in line:
      if char == ' ' or char == '\n':
        count += 1
        
  print(count)

if __name__ == "__main__":
  main()