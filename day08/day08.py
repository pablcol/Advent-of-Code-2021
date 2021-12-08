from collections import Counter

# Import the data, read it and clean it, then put it into a list
reading = open('day08/inputd8.txt', 'r')
data = [x.strip().split("|") for x in reading.readlines()]

# Each segment appears a certain number of times in the digits 0--9
# Each number has a unique pattern of segment occurences.

# So first, build a dictionary mapping segment occurence patterns to
# the numbers they represent.


def occurence_count(s):
    return Counter(list(s.replace(" ", "")))


def occurence_pat(s, ctr):
    return tuple(sorted([ctr[x] for x in s]))


# Digits 0-9 in order according to a particular labelling of segments
canonical_pat = "abcefg cf acdeg acdfg bdcf abdfg abdefg acf abcdefg abcdfg"
canonical_dict = occurence_count(canonical_pat)

# Build the translator dictionary using the canonical pattern to give
# segment occurences
translator = {}
for i, x in enumerate(canonical_pat.split(" ")):
    translator[occurence_pat(x, canonical_dict)] = i

# Then put it to work.


def process_line(ls):
    outputs = ls[1].strip()
    occ_dict = occurence_count(ls[0])
    return [translator[occurence_pat(x, occ_dict)]
            for x in outputs.split(" ")]


part_one = 0
part_two = 0
for lines in data:
    p = process_line(lines)
    part_one += len([x for x in p if x in [1, 4, 7, 8]])
    part_two += int("".join([str(x) for x in p]))


print("Result 1: %s" % part_one)
print("Result 2: %s" % part_two)
