# Create variables for the counts, a list for the input, 2 dictionaries for the
# rates, then open the input text file and split it

binarycount = 0
zerocount = 0
onecount = 0

gammarate = [""]
epsilonrate = [""]

BinaryInput = open("day03/inputd3.txt", "r").read().split()

# Read through each of the inputs, which have a length of 12, and count the
# number of 1s or 0s in each postition, adding them to each counter;

while binarycount < 12:
    for i in BinaryInput:
        if i[binarycount] == "0":
            zerocount += 1
        elif i[binarycount] == "1":
            onecount += 1
# then calculate the rates comparing the number of 1s and 0s: for the gamma the
    if onecount > zerocount:
        gammarate[0] = gammarate[0] + "1"
        epsilonrate[0] = epsilonrate[0] + "0"
    else:
        gammarate[0] = gammarate[0] + "0"
        epsilonrate[0] = epsilonrate[0] + "1"
# finally restart the counters, then continue going through the input by
# increasing the count of the binary
    zerocount = 0
    onecount = 0
    binarycount += 1

# When the input list is over, calculate the overall power consumption by
# multiplying both rates (after converting them to an integer)

powerconsumption = int(gammarate[0], 2) * int(epsilonrate[0], 2)
print(powerconsumption)
