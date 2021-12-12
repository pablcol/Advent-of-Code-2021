from collections import defaultdict
neighbours = defaultdict(list)

for line in open('day12/inputd12.txt', 'r'):
    a, b = line.strip().split('-')
    neighbours[a] += [b]
    neighbours[b] += [a]


def search(part, seen=set(), cave='start'):
    if cave == 'end':
        return 1
    if cave in seen:
        if cave == 'start':
            return 0
        if cave.islower():
            if part == 1:
                return 0
            else:
                part = 1

    return sum(search(part, seen | {cave}, n)
               for n in neighbours[cave])


result1 = search(part=1)
print("Part 1: %s" % result1)

result2 = (search(part=2))
print("Part 2: %s" % result2)
