from random import randint

class Character:

    def __init__(self,skills):
        self.skills = {}


def statroller(Character):
    strength = (randint(1,6) + randint(1,6) + randint(1,6) ) * 5
    Character.strength = strength
    print('str = ',strength)

    cha = (randint(1,6) + randint(1,6) + randint(1,6) ) * 5
    Character.charisma = cha
    print('cha =' ,cha)

    dex = (randint(1,6) + randint(1,6) + randint(1,6) ) * 5
    Character.dexterity = dex
    print('dex = ', dex)

    con = (randint(1,6) + randint(1,6) + randint(1,6) ) * 5
    Character.constitution = con
    print('con = ',con)

    intelligence = (randint(1,6) + randint(1,6) + 6 ) * 5
    Character.intelligence = intelligence
    print('int = ', intelligence)

    appearance = (randint(1,6) + randint(1,6) + randint(1,6) ) * 5
    Character.appearance = appearance
    print('app = ',appearance)



    education = (randint(1,6) + randint(1,6) + 6 ) * 5
    Character.education = education
    print('edu = ', education)

    size = (randint(1,6) + randint(1,6) + 6 ) * 5
    Character.size = size
    print('size = ', size)

    total = strength + cha + dex + con + intelligence + appearance + education + size
    print('stat total = ', total)

def add_skill(Character,skill,value):

    Character.skills[skill] = value


def skill_check(Character,skill):
    roll_result = randint(1,100)
    print("Rolled " + roll_result)
    print("Skill is " + skill)
    if roll_result <= skill:
        print("Passed!")
        if roll_result <= skill * 0.2:
            print("Crit!")
    else:
        print("Failed!")
        if roll_result > 95:
            print("Crit!")

x = Character

statroller(x)