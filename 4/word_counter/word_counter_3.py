def main():
  intput_list = ["Moby", "Dick", "Call", "me", "Ishmael"]
  print(count_words(intput_list))

def count_words(words):
  counts = [0] * len(words)
  file = open("content.txt")
  for line in file:
    line_parts = line.split(" ")
    for part in line_parts:
      for i in range(len(words)):
        if words[i] == part:
          counts[i] += 1

  return counts

        
  print(count)

if __name__ == "__main__":
  main()