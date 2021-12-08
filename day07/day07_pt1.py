# For readeability, create 2 vars, one for reading the input and another one
# for the cleaned input with its data separated, converted to an int
reading = open('day07/inputd7.txt', 'r').read()
cleaninput = [int(x) for x in reading.strip().split(',')]

# Create a list for the result
result = []

# using the initial position, iterate and add all possible combinations, then
# integrate them into the result list
for dest in range(min(cleaninput), max(cleaninput)+1):
    cost = sum(abs(x-dest) for x in cleaninput)
    result.append(cost)

# Then find the min result of that list, which is the cheapest outcome
print(min(result))
