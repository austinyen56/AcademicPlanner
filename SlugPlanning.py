

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


# greetings and main function

print("Welcome to the UCSC Academic Planner!")

# Asking student current quarter


tmpString = 'n'
while tmpString == 'n':
    currentQuarter = input('What is your current quarter?: ')
    currentQuarter = currentQuarter.lower()
    print('Your current quarter is: ', currentQuarter)
    print('Is this correct?: ')

    tmpString = input('type y or n... ')

# Asking student difficulty of classes
print('How do you feel about your classes so far?: ')
currentDiff = input('type, E, M, H: ')
currentDiff = currentDiff.lower()
print('Your current difficulty is set to:', currentDiff)

# Asking students what classes they have taken

tmpString = input('would you like to enter your data manually? y or n: ')
# Taking classes manually and appending to the canTakeClasses
if tmpString == 'y':

    print('What classes have you taken?: ')
    tmpString == 'y'
    while tmpString == 'y':
        print('These are your current taken courses: ')
        print(*classTakenList)

        classes = input('What class have you taken? If no more classes enter n: ')
        if not(classes == 'n'):
            classTakenList.append(classes)
        else:
            tmpString = 'n'

        classTakenList = [classTakenList.lower() for classTakenList in classTakenList]

    # appending classes to can take classes
    for i in sdb.CLASSES.keys():

        if (sub_set(sdb.CLASSES.get(i).get("prereqs"), classTakenList)):
            if currentQuarter in sdb.CLASSES.get("quarter_offered"):
                canTakeClasses.append(i)

# from txt file classes and appending to the canTakeClasses
if tmpString == 'n':
    with open('classes.txt') as f:
        classTakenList = f.read().splitlines()

    # appending classes to can take classes
    for i in sdb.CLASSES.keys():

        if (sub_set(sdb.CLASSES.get(i).get("prereqs"), classTakenList)):
            if currentQuarter in sdb.CLASSES.get("quarter_offered"):
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

# entering command line
while True:
    print('Your planned classes: ', plan)

    user = input('Type commands: ')

    if user == 'help':
        print('-- exit: quits program')
        print('-- help: displays commands')
    if user == 'exit':
        break





