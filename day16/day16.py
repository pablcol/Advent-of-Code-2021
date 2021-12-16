from functools import reduce
from operator import *


with open('day16/inputd16.txt', 'r') as f:
    data = f.read().strip()

bits = [(int(c, 16) >> (3 - i)) & 1 for c in data for i in range(4)][::-1]

as_num = lambda x: sum(2 ** i * b for i, b in enumerate(x[::-1]))


def read_bits(data, n):
    for _ in range(n):
        yield data.pop()


def read_num(data, n):
    return as_num(list(read_bits(data, n)))


vnum_total = 0


def decode(data):
    global vnum_total
    version = read_num(data, 3)
    vnum_total += version
    type_id = read_num(data, 3)
    f = [add, mul, min, max, lambda x, y: 16 * x + y, gt, lt, eq][type_id]

    def get_subpackets():

        if type_id == 4:
            while True:
                done = not data.pop()
                yield read_num(data, 4)
                if done:
                    return
        lid = data.pop()
        if lid:
            for _ in range(read_num(data, 11)):
                yield decode(data)
        else:
            blen = read_num(data, 15)
            l1 = len(data) - blen
            while len(data) != l1:
                yield decode(data)
    return reduce(f, get_subpackets())


print(decode(bits))
print(vnum_total)
