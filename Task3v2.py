import re
initialString = r"""homEwork:
	tHis iz your homeWork, copy these Text to variable. 

	You NEED TO normalize it fROM letter CASEs point oF View. also, create one MORE senTENCE witH LAST WoRDS of each existING SENtence and add it to the END OF this Paragraph.

	it iZ misspeLLing here. fix “iZ” with correct “is”, but ONLY when it Iz a mistAKE. 

	last iz TO calculate nuMber OF Whitespace characteRS in this Text. caREFULL, not only Spaces, but ALL whitespaces. I got 87."""

# convert all text to lower case
lowerString = initialString.lower()

# count whitespaces
whitespaceCount = len(re.findall("\s", lowerString))
print(f'There are {whitespaceCount} whitespaces in the homework.')

# replace mistake with correct 'is'
stringWithoutIz = lowerString.replace(' iz ', ' is ')

# prepare new sentence from last words of all sentences
listwords = []
for word in stringWithoutIz.split():
    if word.endswith('.'):
        word = word.replace('.', '')
        listwords.append(word)
addSentence = ' '.join(listwords) + '.'

# add new sentence to the end of paragraph
position = stringWithoutIz.index('paragraph.')  # index of first letter in the word paragraph.
newText = stringWithoutIz[:position+10] + ' ' + addSentence + stringWithoutIz[position+10:]

# capitalize first letters at the beginning of the line (after tab)
halfFinalText = """"""
for sentence in newText.split('\n\t'):
    halfFinalText += sentence.capitalize() + '\n\t'

# capitalize first letters in the middle of the text (after dot)
finalText = ''
for item in halfFinalText.split('. '):
    finalText += item[0].upper() + item[1:] + '. '
finalText = finalText[:-2]  # remove last unnecessary dot
print(finalText)
