

'''
    Authors: Ted Ikehara and Austin Yen
    Date: Jan 14, 2022

    Main File: This program takes in data and allows the user to optimize their
    decision on what class to take.

    About: This project is for CruzHacks 2022. This is an academic planner
    aiming to help decrease the stress levels of students at University when
    picking classes.
'''
print('loading...')

import slugplanningdb as sdb
import copy
import os
from itertools import combinations

os.system('clear')
print('Finished loading!')

# User info
currentQuarter = ''
currentDiff = ''
classTakenList = []
canTakeClasses = []



# system temp vars
tmpString = ''
tmpInt = 0
tmpBool = True

# l2 is subset of l1
def sub_set(l1, l2):
    tmp = l2[:]
    for i in l1:
        if i in l1:
            if i in tmp:
                tmp.remove(i)
            else:
                return False
    return True

def geReq():
    ge_req = ['cc', 'er', 'im', 'mf', 'si', 'sr', 'ta', 'pee', 'pre', 'c', 'dc']

    with open('classes.txt') as f:
        classTakenList = f.read().splitlines()

    ge_taken = []
    for i in sdb.CLASSES.keys():
        ge_taken.append(sdb.CLASSES.get(i).get("ge_satis"))
    ge_taken_parsed = [j for i in ge_taken for j in i]

    ge_needed = [x for x in ge_req if x not in ge_taken_parsed]
    if not ge_needed:
        print('You satisfied all GEs')
    else:
        print('GE categories needed: ', ge_needed)

# greetings and main function

print("Welcome to the UCSC Academic Planner!")

# Asking student current quarter


tmpString = 'n'
while tmpString == 'n':
    currentQuarter = input('What is your current quarter?: ')
    currentQuarter = currentQuarter
    print('Your current quarter is: ', currentQuarter)
    print('Is this correct?: ')

    tmpString = input('type y or n... ')

# Asking student difficulty of classes
print('How do you feel about your classes so far?: ')
currentDiff = input('type, E, M, H: ')
currentDiff = currentDiff.lower()
print('Your current difficulty is set to:', currentDiff)

# from txt file classes and appending to the canTakeClasses
print('accessing text file... ')
with open('classes.txt') as f:
    classTakenList = f.read().splitlines()

# appending classes to can take classes
for i in sdb.CLASSES.keys():

    if sub_set(sdb.CLASSES.get(i).get("prereqs"), classTakenList):
        if currentQuarter in sdb.CLASSES.get(i).get("quarter_offered"):
            canTakeClasses.append(i)

print('classes that you have take: ', *classTakenList)


# generating combinations of the classes that you can take
classTaken = []
for i in classTakenList:
    classTaken.append(i)

tmpA = classTakenList
tmpB = canTakeClasses

tmpC = []

for elem in copy.deepcopy(tmpA):
    if elem in tmpB:
        tmpA.pop(tmpA.index(elem))
        tmpC.append(tmpB.pop(tmpB.index(elem)))

print('classes you can take: ', *canTakeClasses)

# shows what GEs you still need
geReq()

numClass = int(input('choose the amount of classes you want to take: '))

count = 0
possibleClasses = []



print('\nyour possible options: ')
for i in combinations(canTakeClasses, numClass):
    print(count, '. ', i)

    tmpDiff = []

    # printing out all the class options
    print('The difficulty of these classes: ', end='')
    for j in i:
        diff = sdb.CLASSES.get(j).get('difficulty')
        print(diff, ', ', end='')
        tmpDiff.append(diff)

    diffAvg = sum(tmpDiff)/len(tmpDiff)
    print('\nThe average difficulty is: {:.2f}'.format(diffAvg))

    possibleClasses.append(i)
    count += 1

# generated list of your preffered schedule
tmpInt = int(input('\nChoose by number your preffered schedule: '))
plan = possibleClasses[tmpInt]

os.system('clear')

# all the stats
def stats(cl, inpu):
    return sdb.CLASSES.get(cl).get(inpu)



# entering command line
while True:
    print('Your planned classes: ', plan)

    user = input('Type commands: ')

    if user == 'stats':
        os.system('clear')

        print('Stats of classes: ')


       # flipboard for planned classes

        bo = True
        i = 0

        while bo:

            print(plan[i])
            print('Can you get this class rating: ', stats(plan[i], 'availability'))
            print('General discription of this class: ', stats(plan[i], 'gen_descrip'))
            print('The difficulty of this class is: ', stats(plan[i], 'difficulty'))
            print('The syllabus of the class: ', stats(plan[i], 'syllabus'))
            print('The textbook of the class: ', stats(plan[i], 'textbook'))
            print('Does this class have a lab?: ', stats(plan[i], 'haslab'))
            print('Are the TAs helpful rating?: ', stats(plan[i], 'ta_helpful'))
            print('What is this class focusing on? 0:math, 1:coding, 2:other', stats(plan[i], 'class_type'))
            print('The time commitment rating out of three: ', stats(plan[i], 'time_commit'))
            print('Most people preffer: ', stats(plan[i], 'pref_prof'))

            op = input('press k to go next, j to go back: ')

            if op == 'k':
                i += 1
            if op == 'j':
                i -= 1
            if i >= len(plan):
                i = i % len(plan)
            if not(op == 'j') and not(op == 'k'):
                bo = False

            os.system('clear')

            continue

    if user == 'help':
        print('-- stats: prints all the stats of your planned classes')
        print('-- exit: quits program')
        print('-- help: displays commands')
    if user == 'exit':
        break





