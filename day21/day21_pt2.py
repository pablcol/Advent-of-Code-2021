import functools
import sys
inf = sys.argv[1] if len(sys.argv) > 1 else 'day21/inputd21.txt'

ll = [int(x.split(": ")[1]) for x in open(inf).read().strip().split('\n')]

dice = [
    i + j + k
    for i in (1, 2, 3)
    for j in (1, 2, 3)
    for k in (1, 2, 3)
]


@functools.lru_cache(maxsize=None)
def search(state):
    score, pos = state[0]
    state = [state[1], None]
    wins = [0, 0]
    for roll in dice:
        newpos = (pos + roll - 1) % 10 + 1
        newscore = score + newpos
        state[1] = (newscore, newpos)
        if newscore >= 21:
            wins[0] += 1
        else:
            myself, other = search(tuple(state))
            wins = [wins[0] + other, wins[1] + myself]
    return wins


result = (max(search(((0, ll[0]), (0, ll[1])))))
print("Part 2: %s" % result)
