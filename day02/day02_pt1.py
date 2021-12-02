# Create 2 variables for the horizontal and vertical (depth) counters

horizontal = 0
depth = 0

# Create a list for the input of data and fill it with the input txt file
# and split it by endlines

data = open("day02/inputd2.txt").read().split('\n')[:-1]

# In the loop, navigate the "data" list and whenever it finds a line that
# starts with one of the movements, it adds or subtracts from the counter,
# after converting it to an integer in the appropiate place

for i in data:
    if i.startswith('forward'):
        horizontal += int(i[8:])
    elif i.startswith('down'):
        depth += int(i[5:])
    elif i.startswith('up'):
        depth -= int(i[3:])

print(depth * horizontal)
