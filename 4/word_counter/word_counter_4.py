def main():
  intput_list = get_words("words.txt")
  print(count_words(intput_list))

def get_words(file_name):
  file = open(file_name)
  return_list = []
  for line in file:
    # split up line into a bunch of words
    line = line.split(" ")
    for word in line:
      # remove special chars
      word = word.strip()
      return_list.append(word)

  return return_list

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

if __name__ == "__main__":
  main()