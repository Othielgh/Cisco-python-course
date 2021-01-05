# Your task is to write a program which:

#     asks the user for some text;
#     checks whether the entered text is a palindrome, and prints result.

# Note:

#     assume that an empty string isn't a palindrome;
#     treat upper- and lower-case letters as equal;
#     spaces are not taken into account during the check - treat them as non-existent;
#     there are more than a few correct solutions - try to find more than one.


def paliCheck():
    sentence = input('Please enter a text to check if it\'s a palindrome: ').lower()
    while not sentence:
        sentence = input('Please enter a text to check if it\'s a palindrome: ').lower()
    sentence = sentence.replace(' ', '')

    if str(sentence) == str(sentence)[::-1]:
        print('It\'s a palindrome!')
    elif sentence == '':
        print('Please enter something!')
    else:
        print('This is not a palindrome!')

paliCheck()