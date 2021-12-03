# Create variables for the counts, 2 lists for the input, a dictionary for the
# rate, 2 blank strings for the binaries and then open the input text file,
# split it and re-use it to the CO2 list

binarycount = 0
zerocount = 0
onecount = 0

epsilonrate = [""]

realbinary = ""
co2binary = ""

o2binarylist = open("day03/inputd3.txt", "r").read().split()
co2binarylist = o2binarylist

# Read through each of the 1st bit of the inputs, which have a length of 12,
# and count the 1s and 0s separately, adding them to each counter, then,
# follwing the criteria for o2: most common value (if 0s and 1s eq. common,
# then keep only 1s), it gets added to the final list

while binarycount < 12:
    for i in o2binarylist:
        if i[binarycount] == "0":
            zerocount += 1
        elif i[binarycount] == "1":
            onecount += 1

    if zerocount > onecount:
        realbinary += "0"
    elif onecount > zerocount or onecount == zerocount:
        realbinary += "1"

    if len(o2binarylist) > 1:
        o2binarylist = [x for x in o2binarylist if x.startswith(realbinary)]

    zerocount = 0
    onecount = 0
    binarycount += 1

binarycount = 0

# Same as previously, but the criteria is now reversed: the least common value
# (if 0s and 1s eq. common, then keep only 0s), gets added to the final list

while binarycount < 12:
    for u in co2binarylist:
        if u[binarycount] == "0":
            zerocount += 1
        elif u[binarycount] == "1":
            onecount += 1

    if zerocount > onecount:
        co2binary += "1"
    elif onecount > zerocount or onecount == zerocount:
        co2binary += "0"

    if len(co2binarylist) > 1:
        co2binarylist = [x for x in co2binarylist if x.startswith(co2binary)]

    zerocount = 0
    onecount = 0
    binarycount += 1

# To get the rating, it gets multiplied together, after its converted to an int

lifesupportrating = int(o2binarylist[0], 2) * int(co2binarylist[0], 2)
print(lifesupportrating)
