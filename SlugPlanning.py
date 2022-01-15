

'''
    Authors: Ted Ikehara and Austin Yen
    Date: Jan 14, 2022

    Main File: This program takes in data and allows the user to optimize their
    decision on what class to take.

    About: This project is for CruzHacks 2022. This is an academic planner
    aiming to help decrease the stress levels of students at University when
    picking classes.
'''

import slugplanningdb as sdb

# User info
currentQuarter = ''
currentDiff = ''
classTakenList = []
canTakeClasses = []



# system temp vars
tmpString = ''
tmpInt = 0
tmpBool = True


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

for i in sdb.CLASSES.keys():

    if sub_set(sdb.CLASSES.get(i).get("prereqs"), classTakenList):
        canTakeClasses.append(i)


print('classes you can take: ', *canTakeClasses)






