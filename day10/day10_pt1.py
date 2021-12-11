ll = [x for x in open('day10/inputd10.txt', 'r').read().strip().split('\n')]

matches = {'[': ']', '{': '}', '<': '>', '(': ')'}
costs = {']': 57, ')': 3, '}': 1197, '>': 25137}
starters = list(matches.keys())
for (k, v) in list(matches.items()):
    matches[v] = k
cost = 0
for line in ll:
    stack = []
    for ch in line:
        if ch in starters:
            stack = [ch] + stack
        else:
            if not stack:
                break
            expected = matches[stack[0]]
            stack = stack[1:]
            if expected == ch:
                continue
            cost += costs[ch]
            break
print(cost)
