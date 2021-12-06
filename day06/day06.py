initialPop = int(input())


def LanternFish(days):
    inputF = open('day06/inputd6.txt', 'r').readlines()

    fishpopulation = []
    for i in range(9):
        fishpopulation.append(inputF[0].count(str(i)))
    counter = 0
    while counter < days:
        newpop = [0, 0, 0, 0, 0, 0, 0, 0, 0]
        day = 1
        while day < len(fishpopulation):
            # shift everything left
            newpop[day - 1] = fishpopulation[day]
            day += 1
        # put the new fish at the back
        newpop[8] = fishpopulation[0]
        # put the mother fish at 7 days away
        newpop[6] += fishpopulation[0]
        fishpopulation = newpop
        counter += 1
    print(sum(fishpopulation))


LanternFish(initialPop)
