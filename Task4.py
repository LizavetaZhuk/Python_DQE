import random
import re


# Task2
# function to create a list of random number of dicts (from 2 to 10)
def random_list():
    randomlist = []
    for n in range(random.randint(2, 10)):
        letters = 'abcdefghijklmnopqrstuvwxyz'
        randomKeyList = []
        randomDict = {}
        for i in range(random.randint(1, 26)):
            key = letters[random.randint(0, 25)]
            randomKeyList += key
        for letter in randomKeyList:
            randomDict[letter] = random.randint(1, 100)
        randomlist.append(randomDict)
    return randomlist


# finction to merge all dicts in the list to one dict with correct names
def common_list(param):
    randomlist = random_list()
    commonDict = {}
    key_entry = {}
    finalDict = {}
    for index, dict in enumerate(randomlist):
        for key in dict.keys():
            if key not in commonDict:
                commonDict[key] = dict[key]
                key_entry[key] = 1
            elif commonDict[key] < dict[key]:
                commonDict[key] = dict[key]
                key_entry[key] = index + 1
        for i in commonDict:
            if key_entry.get(i) > 1:
                finalDict[str(i) + '_' + str(key_entry.get(i))] = commonDict.get(i)
            else:
                finalDict[i] = commonDict.get(i)
    return finalDict


# main function which use 2 previous functions
def main_func_task2():
    x = random_list()
    return common_list(x)


print(main_func_task2())

# Task3

initialString = r"""homEwork:
	tHis iz your homeWork, copy these Text to variable. 

	You NEED TO normalize it fROM letter CASEs point oF View. also, create one MORE senTENCE witH LAST WoRDS of each existING SENtence and add it to the END OF this Paragraph.

	it iZ misspeLLing here. fix “iZ” with correct “is”, but ONLY when it Iz a mistAKE. 

	last iz TO calculate nuMber OF Whitespace characteRS in this Text. caREFULL, not only Spaces, but ALL whitespaces. I got 87."""


# function to count whitespaces in the text
def whs_count_func(text):
    whitespaceCount = len(re.findall("\s", text))
    return f'There are {whitespaceCount} whitespaces in the homework.'


# function to normalize text to letter case point of view
def normalize_func(text):
    halffinaltext = """"""
    finalText = ''

    # convert all text to lower case
    lowerString = initialString.lower()

    # replace mistake with correct 'is'
    stringWithoutIz = lowerString.replace(' iz ', ' is ')

    # capitalize first letters at the beginning of the line (after tab)
    for sentence in stringWithoutIz.split('\n\t'):
        halffinaltext += sentence.capitalize() + '\n\t'

    # capitalize first letters in the middle of the text (after dot)
    for item in halffinaltext.split('. '):
        finalText += item[0].upper() + item[1:] + '. '
    finalText = finalText[:-2]  # remove last unnecessary dot
    return finalText


# function ti prepare new sentence from last words of all sentences and add it to the middle of text
def add_sentence_func(text):
    lowertext = text.lower()
    last_words = re.findall(r"\w+(?=[.])", lowertext)
    addsentence = ' '.join(last_words) + '.'

    position = lowertext.index('paragraph.')  # index of first letter in the word paragraph.
    newText = lowertext[:position + 10] + ' ' + addsentence + lowertext[position + 10:]
    return newText


# function to normalize text and add new sentence
def main_func_task3(text):
    x = add_sentence_func(text)
    return normalize_func(x)


print(whs_count_func(initialString))
print(main_func_task3(initialString))
