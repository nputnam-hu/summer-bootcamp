import bootcamp

# Gets height of pyramid
while True:
    height = bootcamp.get_int("height?")
    if height > 0 and height <= 23:
        break
    else:
        print("retry: ", end = "")
        
# creates pyramid
for row in range(height):
    # creates left space and blocks
    for left_blank in range(height - 1 - row):
        print(" ", end = "")
    for left_block in range(row + 1):
        print("#", end = "")
    # creates two space in middle of pyramid
    print("  ", end = "")
    # creates right space and blocks
    for right_block in range(row + 1):
        print("#", end = "")
    for right_blank in range(height - 1 - row):
        print(" ", end = "")
    # move to next row
    print()