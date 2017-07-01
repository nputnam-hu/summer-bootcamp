def main():
  count_words("Moby")

def count_words(word):
  count = 0
  file = open("content.txt")
  for line in file:
    line_parts = line.split(" ")
    for part in line_parts:
      if part == word:
        count += 1
        
  print(count)

if __name__ == "__main__":
  main()