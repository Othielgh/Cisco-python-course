# Scenario

# Let's play a game. We will give you two strings: one being a word (e.g., "dog") and the second being a combination of any characters.

# Your task is to write a program which answers the following question: are the characters comprising the first string hidden inside the second string?

# For example:

#     if the second string is given as "vcxzxduybfdsobywuefgas", the answer is yes;
#     if the second string is "vcxzxdcybfdstbywuefsas", the answer is no (as there are neither the letters "d", "o", or "g", in this order)

# Hints:

#     you should use the two-argument variants of the pos() functions inside your code;  there is no pos()???
#     don't worry about case sensitivity.

firstWord = list(input('Please enter the word you want to find: '))
secondWord = list(input('Please enter the letters to check: '))

def findWord(firstWord, secondWord):
    print('Is', ''.join(firstWord), 'in', ''.join(secondWord), '?')
    if 0 in [c in firstWord for c in secondWord]:
        print('Yes')
    else:
        print('No')


findWord(firstWord,secondWord)

