from random import randint

def bigrole(num):

    total = 0
    ctr = 0
    rolllist = []
    while ctr < num:
        roll = randint(1,6)
        #print(roll)
        rolllist.append(roll)
        total += roll
        ctr += 1

    total -= min(rolllist)

    return total


def smallrole(num):

    total = 0
    ctr = 0
    while ctr < num:
        roll = randint(1,6)
        total += roll
        ctr += 1

    return total


def listbuilder(num):
        resultlist = []
        bigger = bigrole(num+1)
        smaller = smallrole(num)
        return bigger/smaller


def tester(iterations):
    testlist = []
    testtotal = 0
    for n in range(1,iterations):
        #print(n)
        testlist.append(listbuilder(3))

    for n in testlist:
        #print(n)
        if isinstance(n,float):
            testtotal += n

    testtotal = testtotal / len(testlist)
    return testtotal

#print(11/7)

print(tester(1000000))

'''
 def listbuilder(num):
        resultlist = []
        bigger = bigrole(num+1)
        smaller = smallrole(num)
        return bigger/smaller
'''







