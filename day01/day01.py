# This takes some data in the form of a txt file, reads it separated by lines,
# converts it to int values and then puts it in a python dictionary

import numpy as np

data = [int(n) for n in open("day01/inputd1.txt").readlines()]


# This function for the first ex, takes the values stored in data, and checks
# for any increase in two consecutive numbers, then adds them all together
def ex01(d):
    return sum((np.array(d) - np.append([0], np.array(d[:-1]))) > 0) - 1


print(ex01(data))

# This funciton for the 2nd ex takes the result of the conovlution (mod) of the
# data, in 3 increments and passes it to the first function in order to get


def increaseWindow(d, wsize=3):
    w = np.convolve(np.array(d), np.ones(wsize), 'valid')
    return ex01(w)


print(increaseWindow(data))
