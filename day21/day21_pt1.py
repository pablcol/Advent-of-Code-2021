import sys
inf = sys.argv[1] if len(sys.argv) > 1 else 'day21/inputd21.txt'

pos = [int(x.split(": ")[1]) for x in open(inf).read().strip().split('\n')]

dice = 1
score = [0, 0]
done = False
while not done:
    for player in range(2):
        newpos = (pos[player] + dice + dice + 1 + dice + 2 - 1) % 10 + 1
        dice += 3
        score[player] += newpos
        pos[player] = newpos
        if score[player] >= 1000:
            result = (score[1-player]*(dice-1))
            done = True
            break

print("Part 1: %s" % result)
