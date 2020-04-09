"""
This exercise stub and the test suite contain several enumerated constants.

Since Python 2 does not have the enum module, the idiomatic way to write
enumerated constants has traditionally been a NAME assigned to an arbitrary,
but unique value. An integer is traditionally used because it’s memory
efficient.
It is a common practice to export both constants and functions that work with
those constants (ex. the constants in the os, subprocess and re modules).

You can learn more here: https://en.wikipedia.org/wiki/Enumerated_type
"""
def full_house(dice):
    '''Full House 	Total of the dice 	Three of one number and two of another 	3 3 3 5 5 scores 19'''
    three,two=[],[]
    for i in dice:
        if dice.count(i) == 3:
            three.append(i)
        if dice.count(i) == 2:
            two.append(i)

    if len(three) == 3 and len(two) == 2:
        return sum(three + two)
    return 0
def yacht(dice):
    if dice[0]==dice[1]==dice[2]==dice[3]==dice[4]:
        return 50
    return 0
def four_of_a_kind(dice):
    for i in dice:
        if dice.count(i) >= 4:
            return i*4
    return 0
def little_straight(dice):
    if ''.join(sorted(map(str,dice)))=='12345':
        return 30
    return 0    

def big_straight(dice):
    if ''.join(sorted(map(str,dice)))=='23456':
        return 30
    return 0

YACHT = yacht 
ONES = lambda dice : 1 * dice.count(1)
TWOS = lambda dice : 2 * dice.count(2)
THREES = lambda dice : 3 * dice.count(3)
FOURS = lambda dice : 4 * dice.count(4)
FIVES = lambda dice : 5 * dice.count(5)
SIXES = lambda dice : 6 * dice.count(6)
CHOICE = lambda dice : sum(dice)
FULL_HOUSE = full_house
FOUR_OF_A_KIND = four_of_a_kind   
LITTLE_STRAIGHT = little_straight
BIG_STRAIGHT = big_straight


def score(dice, category):
    
    test=category(dice)    
    if test:
        return test
    return 0
print(score([2, 2, 4, 4, 4], FULL_HOUSE))