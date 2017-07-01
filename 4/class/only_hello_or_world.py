
valid_words = ["hello", "world"]
file = open("sample.txt")
for line in file:
  line = line.strip()
  if line in valid_words:
    print(line)




    