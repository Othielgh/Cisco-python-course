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
    newWord = ''
    print('Is', ''.join(firstWord), 'in', ''.join(secondWord), '?')
    for s in secondWord:
        for item in firstWord:
            if item in s:
                print('found'), item
                item += newWord
            else:
                print('No')
                break
        if newWord is firstWord:
            print('yes')
        else:
            print('no')


findWord(firstWord,secondWord)

