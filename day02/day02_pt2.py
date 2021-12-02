# Create 3 variables for the horizontal and vertical (depth) counters
# and for the aim

horizontal = 0
depth = 0
aim = 0

# Create the same list for the input of data and fill it with the input
# txt file and split it by endlines

data = open("day02/inputd2.txt").read().split('\n')[:-1]

# In the loop, navigate the "data" list and whenever it finds a line that
# starts with one of the depth movements, it increases the aim value and if
# it is the forward movement, it changes the depth value by multiplying it
# with said aim, then stores it in the appropiate value after converting it
# to an integer in the appropiate place

for lines in data:
    if lines.startswith('forward'):
        horizontal += int(lines[8:])
        depth += aim * int(lines[8:])
    elif lines.startswith('down'):
        aim += int(lines[5:])
    elif lines.startswith('up'):
        aim -= int(lines[3:])

print(depth * horizontal)
