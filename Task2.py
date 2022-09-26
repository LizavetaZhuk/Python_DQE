# Part 1

import random

# block of code to create a list of random number of dicts (from 2 to 10)
randomlist = []
for n in range(random.randint(2, 10)):  # how many dicts will be in the list from 2 to 10

    # block of code to prepare random list of future Keys
    letters = 'abcdefghijklmnopqrstuvwxyz'
    randomKeyList = []
    for i in range(random.randint(1, 26)):  # how many letters will be in the list from 1 to 26
        key = letters[random.randint(0, 25)]  # get random letter from letters
        randomKeyList += key  # add this random letter to the list, repeat i times
    # print (randomKeyList)

    # block of code to create a random dictionary using randomKeyList and add it to the list
    randomDict = {}
    for letter in randomKeyList:
        randomDict[letter] = random.randint(1, 100)  # add a random value from 1 to 100 to each key in the list
    # print (randomDict)
    randomlist.append(randomDict)

# print(randomlist)


# Part 2

# block of code to merge all dicts in the list to one dict
commonDict = {}
for i in range(len(randomlist)):  # how many dicts in the list = how many times iterate i
    dict = randomlist[i]  # assign one single dict from list
    for key, value in dict.items():
        if key not in commonDict:
            commonDict[key] = [value, i, 0]  # value for the key is a list. 0 - flag that key met for the first time
        elif key in commonDict and commonDict[key][0] < value:
            commonDict[key] = [value, i, 1]  # 1 - flag that the key was already met in other dict and value changed
        elif key in commonDict and commonDict[key][0] >= value:
            commonDict[key][2] = 2  # 2 - flag that the key was already met in other dict and value NOT changed
# print(commonDict)

# block of code to format key name and value and sort by key
finalDict = {}
for key, value in commonDict.items():
    if commonDict[key][1] == 0 and commonDict[key][2] == 2:  # format key where the very first key was max
        finalDict[key + '_' + str(commonDict[key][1]+1)] = commonDict[key][0]  # add '_1' and correct value as int
    elif commonDict[key][2] == 0:  # format key which met only once among all dicts
        finalDict[key] = commonDict[key][0]  # format key without changes, add correct value as int
    else:  # for other key add number of dict and correct max value as int
        finalDict[key + '_' + str(commonDict[key][1]+1)] = commonDict[key][0]  # i position of dict + 1 (human count)
# print(finalDict)
orderedFinalDict = sorted(finalDict)
print(orderedFinalDict)