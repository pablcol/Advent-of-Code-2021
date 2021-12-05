input = open('day05/inputd5.txt', 'r')
data = [line.strip().split(" -> ") for line in input.readlines()]
vents = list(map(lambda x: [tuple(int(i) for i in x[0].split(",")),
                            tuple(int(i) for i in x[1].split(","))],
                 data))

part1vents = [vent for vent in vents if vent[0][0] == vent[1][0] or
              vent[0][1] == vent[1][1]]

total_points_covered = set()
overlaps = set()

for vent in part1vents:
    start, end = vent
    if start[0] == end[0]:
        if start[1] > end[1]:
            points_covered = ((start[0], x) for x in range(end[1], start[1]+1))
        else:
            points_covered = ((start[0], x) for x in range(start[1], end[1]+1))
    elif start[1] == end[1]:
        if start[0] > end[0]:
            points_covered = ((x, start[1]) for x in range(end[0], start[0]+1))
        else:
            points_covered = ((x, start[1]) for x in range(start[0], end[0]+1))

    for point in points_covered:
        if point in total_points_covered:
            overlaps.add(point)
        else:
            total_points_covered.add(point)

print(len(overlaps))
