import random
import numpy as np

class Player(object):
    def __init__(self, num, func):
        self.number = num
        self.func = func

    def show(self):
        print("player num:", self.number)

NUMofPLAYERS = 19
ROUND = 1
MYchoices = []
OTHERchoices = []
MYpayoffs = []
OTHERpayoffs = []

def DpercentNstepsBACK( OTHERchoice, n, t ):
    if n > t:
        n = t
    print (OTHERchoice[t - n:t])
    tempOTHER = list(filter(lambda cho: cho == 'D', OTHERchoice[t-n:t]))

    return len(tempOTHER) / len(OTHERchoice)

def f1(OTHERchoice, MYchoice, OTHERpayoff, MYpayoff, t):
    return 'D'

def f2(OTHERchoice, MYchoice, OTHERpayoff, MYpayoff, t):
    return 'C'

def f3(OTHERchoice, MYchoice, OTHERpayoff, MYpayoff, t):
    choice = random.randint(0, 1)
    if choice:
        return 'C'
    else:
        return 'D'

def f4(OTHERchoice, MYchoice, OTHERpayoff, MYpayoff, t):
    choice = 'a'
    if t == 0:
        choice = 'D'
    else:
        summaryOTHERPayoffs = sum(OTHERpayoff)
        summaryMYPayoffs = sum(MYpayoff)
        tempOTHER = list(filter(lambda cho: cho == 'D', OTHERchoice))
        DOTHERpercentage = len(tempOTHER) / len(OTHERchoice)

        tempMY = list(filter(lambda cho: cho == 'D', MYchoice))
        DMYpercentage = len(tempMY) / len(MYchoice)

        if DOTHERpercentage > 0.4 and t > 50:
            choice = 'D'

        if DOTHERpercentage > 0.9:
            choice = 'D'

        elif OTHERchoice[t-1] == 'C' and MYchoice[t-1] == 'D':
            choice = 'D'
        elif OTHERchoice[t-1] == 'D' and MYchoice[t-1] == 'D':
            choice = 'C'
        elif OTHERchoice[t-1] == 'C' and MYchoice[t-1] == 'C':
            choice = 'C'
        elif OTHERchoice[t-1] == 'D' and MYchoice[t-1] == 'C':
            choice = 'D'

        print('DMYpercentage: ', DMYpercentage)
        print('DOTHERpercentage: ', DOTHERpercentage)

    return choice

def f5(OTHERchoice, MYchoice, OTHERpayoff, MYpayoff, t):
    choice = 'a'
    if t == 0:
        choice = 'D'
    else:
        summaryOTHERPayoffs = sum(OTHERpayoff)
        summaryMYPayoffs = sum(MYpayoff)

        DOTHERpercentage = DpercentNstepsBACK(OTHERchoice, 30, t)

        tempMY = list(filter(lambda cho: cho == 'D', MYchoice))
        DMYpercentage = len(tempMY) / len(MYchoice)

        if DOTHERpercentage > 0.4 and t > 50:
            choice = 'D'

        if DOTHERpercentage > 0.9:
            choice = 'D'

        DOTHERpercentage = DpercentNstepsBACK(OTHERchoice, 5, t)
        if DOTHERpercentage < 0.1 and t % 4 == 0:
            choice = 'D'
        elif DOTHERpercentage < 0.1:
            choice = 'C'


        if OTHERchoice[t-1] == 'C' and MYchoice[t-1] == 'D':
            choice = 'D'
        elif OTHERchoice[t-1] == 'D' and MYchoice[t-1] == 'D':
            choice = 'C'
        elif OTHERchoice[t-1] == 'C' and MYchoice[t-1] == 'C':
            choice = 'C'
        elif OTHERchoice[t-1] == 'D' and MYchoice[t-1] == 'C':
            choice = 'D'

        print('DMYpercentage: ', DMYpercentage)
        print('DOTHERpercentage: ', DOTHERpercentage)

    return choice

Players = [Player(1, f1), Player(2, f2), Player(3, f3), Player(4, f4), Player(5, f5)]

for step in range(200):
    firstPCHOICE = Players[3].func(OTHERchoices, MYchoices, OTHERpayoffs, MYpayoffs, step)
    MYchoices.append(firstPCHOICE)


    thirdPCHOICE = Players[4].func(OTHERchoices, MYchoices, OTHERpayoffs, MYpayoffs, step)
    OTHERchoices.append(thirdPCHOICE)

    if firstPCHOICE == 'C' and thirdPCHOICE == 'C':
        MYpayoffs.append(3)
        OTHERpayoffs.append(3)
    elif firstPCHOICE == 'C' and thirdPCHOICE == 'D':
        MYpayoffs.append(0)
        OTHERpayoffs.append(5)
    elif firstPCHOICE == 'D' and thirdPCHOICE == 'C':
        MYpayoffs.append(5)
        OTHERpayoffs.append(0)
    elif firstPCHOICE == 'D' and thirdPCHOICE == 'D':
        MYpayoffs.append(1)
        OTHERpayoffs.append(1)
    summaryOTHERPayoffs = sum(OTHERpayoffs)
    summaryMYPayoffs = sum(MYpayoffs)

print(MYchoices)
print(MYpayoffs)
print(summaryMYPayoffs)


print(OTHERchoices)
print(OTHERpayoffs)
print(summaryOTHERPayoffs)


