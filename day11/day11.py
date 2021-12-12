data = open('day11/inputd11.txt', 'r').read()


def load_grid(data):
    D = {}
    for y, line in enumerate(data.split()):
        for x, c in enumerate(line):
            D[complex(x, -y)] = int(c)
    return D


def tick(grid):
    for k in grid:
        grid[k] += 1
    flashed = set()
    toflash = {k for k, v in grid.items() if v > 9}
    while toflash:
        flashed.update(toflash)
        for k in toflash:
            for delta in [1, 1+1j, 0+1j, -1+1j, -1, -1-1j, 0-1j, 1-1j]:
                try:
                    grid[k+delta] += 1
                except KeyError:
                    pass
        toflash = {k for k, v in grid.items() if v > 9 and k not in flashed}
    for k in flashed:
        grid[k] = 0
    return len(flashed)


grid = load_grid(data)
flashes = sum(tick(grid) for _ in range(100))
print("Part 1: %s" % flashes)

grid = load_grid(data)
i = 1
while tick(grid) < 100:
    i += 1
print("Part 2: %s " % i)
