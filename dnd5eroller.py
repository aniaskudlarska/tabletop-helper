from random import randint

class DND5Echar:

    def __init__(self,stats,skills,race,charclass,inventory,level):

        stats = {}
        skills = []
        race = str
        charclass = str
        inventory = str
        level = int



def statroller():
    '''quick statroll - prints stats'''
    console = False
    while console is not True:
        dice = int
        prompt = input('4d6 drop lowest or 3d6? ')

        if prompt == '3d6':
            dice = 0

        if prompt == '4d6':
            dice = 1

        if prompt == 'quit':
            console = True
        skilllist = ['str', 'con', 'dex', 'cha', 'int', 'wis']

        if dice == 0:
            for item in skilllist:
                print(item + ' = ' + str((roll_dice(3,6))))
        if dice == 1:
            for item in skilllist:
                print(item + ' = ' + (drop_lowest_roll(4,6)))

def roll_dice(number,sides):
        total = 0
        counter = 0
        while counter < number:
            roll = randint(1,sides)
            total += roll
            counter += 1

        return total

def drop_lowest_roll(number,sides):
    total = 0
    counter = 0
    rolllist = []
    while counter < number:
        roll = randint(1, sides)
        rolllist.append(roll)
        total += roll
        counter += 1

    return str(total - min(rolllist))



statroller()