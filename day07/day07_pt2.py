# Second part is essentially the same on the first steps, same data treatment
reading = open('day07/inputd7.txt', 'r').read()
cleaninput = [int(x) for x in reading.strip().split(',')]

# Same list for the result
result = []


# Now the cost of fuel increases linearly
def fuel(a):
    return a*(a+1)//2


# Same iterations, but now accounting for the increase in fuel cost
for dest in range(min(cleaninput), max(cleaninput)+1):
    cost = sum([fuel(abs(x-dest)) for x in cleaninput])
    result.append(cost)

# Then find the min result of that list, which is the cheapest outcome
print(min(result))
