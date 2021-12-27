import sys
import re

infile = sys.argv[1] if len(sys.argv) > 1 else 'day22/inputd22.txt'
data = open(infile).read().strip()

X = set()
Y = set()
Z = set()
C = []
min_x = 0
min_y = 0
min_z = 0
max_x = 0
max_y = 0
max_z = 0
G = set()

for r, line in enumerate(data.strip().split('\n')):
    assert line == line.strip()
    words = line.split()
    cmd = words[0]
    x1, x2, y1, y2, z1, z2 = [int(x) for x in re.findall('-?\d+', words[1])]
    x1, x2 = min(x1, x2), max(x1, x2)
    y1, y2 = min(y1, y2), max(y1, y2)
    z1, z2 = min(z1, z2), max(z1, z2)

    X.add(x1)
    X.add(x2+1)
    Y.add(y1)
    Y.add(y2+1)
    Z.add(z1)
    Z.add(z2+1)

    min_x = min(x1, min_x)
    min_y = min(y1, min_y)
    min_z = min(z1, min_z)
    max_x = max(x2, max_x)
    max_y = max(y2, max_y)
    max_z = max(z2, max_z)
    C.append((x1, x2, y1, y2, z1, z2, cmd == 'on'))


def expand(aa):
    bb = set()
    for x in aa:
        bb.add(x)
    bb = sorted(bb)

    ret = {}
    u = {}
    len_sum = 0
    for i, x in enumerate(bb):
        ret[x] = i
        if i+1 < len(bb):
            len_ = bb[i+1]-x if i+1 < len(bb) else None
            len_sum += len_
            u[i] = len_
    for a in aa:
        assert a in ret
    assert len_sum == max(bb)-min(bb), f'{len_sum} {max(bb)-min(bb)}'
    return ret, u


X.add(-50)
X.add(51)
Y.add(-50)
Y.add(51)
Z.add(-50)
Z.add(51)

X, UX = expand(X)
Y, UY = expand(Y)
Z, UZ = expand(Z)


def solve(p1):
    g = set()
    for t, (x1, x2, y1, y2, z1, z2, on) in enumerate(C):
        if p1:
            x1 = max(x1, -50)
            y1 = max(y1, -50)
            z1 = max(z1, -50)
            x2 = min(x2, 50)
            y2 = min(y2, 50)
            z2 = min(z2, 50)
        for x in range(X[x1], X[x2+1]):
            for y in range(Y[y1], Y[y2+1]):
                for z in range(Z[z1], Z[z2+1]):
                    if on:
                        g.add((x, y, z))
                    else:
                        g.discard((x, y, z))

    ans = 0
    for x, y, z in g:
        lx = UX[x]
        ly = UY[y]
        lz = UZ[z]
        ans += lx*ly*lz
    return ans


sol = solve(True)
print("Part 1: %s" % sol)
sol = solve(False)
print("Part 2: %s" % sol)
