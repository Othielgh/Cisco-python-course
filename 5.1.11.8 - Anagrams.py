# Your task is to write a program which:

#     asks the user for two separate texts;
#     checks whether, the entered texts are anagrams and prints the result.

# Note:

#     assume that two empty strings are not anagrams;
#     treat upper- and lower-case letters as equal;
#     spaces are not taken into account during the check - treat them as non-existent

def anagram():
    # Keep going until theres an input
    while True:
        firstWord = input('Please enter the first word: ').lower()
        if not firstWord:
            continue
        else:
            break
    while True:
        secondWord = input('Please enter the second word: ').lower()
        if not secondWord:
            continue
        else:
            break

    # Just sort the letters, then check if they're the same
    firstWord = sorted(firstWord)
    secondWord = sorted(secondWord)
    if firstWord == secondWord:
        print('It\'s an angaram')
    else:
        print('Not an anagram')


anagram()
    
