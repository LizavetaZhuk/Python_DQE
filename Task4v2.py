import random
import re


# Task2
# function to create a list of random number of dicts
def random_list_func(a, b):
    randomlist = []
    for n in range(random.randint(a, b)):
        letters = 'abcdefghijklmnopqrstuvwxyz'
        randomkeylist = []
        randomdict = {}
        for i in range(random.randint(1, 26)):
            key = letters[random.randint(0, 25)]
            randomkeylist += key
        for letter in randomkeylist:
            randomdict[letter] = random.randint(1, 100)
        randomlist.append(randomdict)
    return randomlist


# function to merge all dicts in the list to one dict with correct names
def common_list_func(param):
    randomlist = param
    commondict = {}
    finaldict = {}
    for i in range(len(param)):
        dict = param[i]
        for key, value in dict.items():
            if key not in commondict:
                commondict[key] = [value, i, 0]
            elif key in commondict and commondict[key][0] < value:
                commondict[key] = [value, i, 1]
            elif key in commondict and commondict[key][0] >= value:
                commondict[key][2] = 2
    for key, value in commondict.items():
        if commondict[key][1] == 0 and commondict[key][2] == 2:
            finaldict[key + '_' + str(commondict[key][1] + 1)] = commondict[key][0]
        elif commondict[key][2] == 0:
            finaldict[key] = commondict[key][0]
        else:
            finaldict[key + '_' + str(commondict[key][1] + 1)] = commondict[key][0]
    return finaldict


# main function which use 2 previous functions
def main_func_task2(a=2, b=10):  # default arguments
    x = random_list_func(a, b)
    return common_list_func(x)


print(main_func_task2())  # can be passed other number of dict


# Task3

initialString = r"""homEwork:
	tHis iz your homeWork, copy these Text to variable. 

	You NEED TO normalize it fROM letter CASEs point oF View. also, create one MORE senTENCE witH LAST WoRDS of each existING SENtence and add it to the END OF this Paragraph.

	it iZ misspeLLing here. fix “iZ” with correct “is”, but ONLY when it Iz a mistAKE. 

	last iz TO calculate nuMber OF Whitespace characteRS in this Text. caREFULL, not only Spaces, but ALL whitespaces. I got 87."""


# function to count whitespaces in the text
def whs_count_func(text):
    whitespacecount = len(re.findall("\s", text))
    return f'There are {whitespacecount} whitespaces in the homework.'


# function to normalize text to letter case point of view
def normalize_func(text):
    halffinaltext = """"""
    finaltext = ''

    # capitalize first letters at the beginning of the line (after tab)
    for sentence in text.split('\n\t'):
        halffinaltext += sentence.capitalize() + '\n\t'

    # capitalize first letters in the middle of the text (after dot)
    for item in halffinaltext.split('. '):
        finaltext += item[0].upper() + item[1:] + '. '
    finaltext = finaltext[:-2]  # remove last unnecessary dot
    return finaltext


# function to replace mistake 'iz' with correct 'is'
def replace_iz_func(text):
    lowerstring = text.lower()
    stringwithoutiz = lowerstring.replace(' iz ', ' is ')
    return stringwithoutiz


# function ti prepare new sentence from last words of all sentences and add it to the middle of text
def add_sentence_func(text):
    lowertext = text.lower()
    last_words = re.findall(r"\w+(?=[.])", lowertext)
    addsentence = ' '.join(last_words) + '.'

    position = lowertext.index('paragraph.')  # index of first letter in the word paragraph.
    newtext = lowertext[:position + 10] + ' ' + addsentence + lowertext[position + 10:]
    return newtext


# function to normalize text and add new sentence
def main_func_task3(text):
    x = replace_iz_func(text)
    y = add_sentence_func(x)
    return normalize_func(y)


try:
    print(whs_count_func(initialString))
    print(main_func_task3(initialString))
except ValueError:
    print("You forgot to pass argument to the function!")
