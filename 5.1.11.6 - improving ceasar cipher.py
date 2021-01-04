# Your task is to write a program which:

#     asks the user for one line of text to encrypt;
#     asks the user for a shift value (an integer number from the range 1..25 - note: you should force the user to enter a valid shift value (don't give up and don't let bad data fool you!)
#     prints out the encoded text. 

# Test your code using the data we've provided.
# Test data

# Sample input:
# abcxyzABCxyz 123
# 2

# Sample output:
# cdezabCDEzab 123

# Sample input:
# The die is cast
# 25

# Sample output:
# Sgd chd hr bzrs


## what to do :
#     Make a list of characters?
#     Calculate the position/index of the character in the 0-25 range. (ASCII?)
#     Perform the positive shift using the modulo operation.
#     Find the character at the new position.
#     Replace the current character by this new character.

import string

encryption = ''
alphabet = string.ascii_lowercase #instead of typing a list, also not using ascii_letters because of the shifting required
alphabetCapital = string.ascii_uppercase


def encrypt():
    message = input("Enter the message you would like to encrypt: ")
    #empty string to hold answer
    encryption = ''
    #Made a while loop to catch errors without stopping the program
    while True:
        try:
            key = int(input("Enter key to encrypt: "))
            if key <1 or key > 25:
                print('Please enter a valid number (1-25)')
                continue
            if not key:
                raise ValueError
            else:
                break
        except ValueError:
            print('Please enter a number')
            
    # Check if character is Upper or Lower case, then shift its position. If neither, just add it as is.
    for char in message:
        if char in alphabet:
            position = alphabet.find(char)
            newPosition = (position + key) % 26 # Modulate by 26 because amount of characters in alphabet
            newChar = alphabet[newPosition]
            encryption += newChar
        elif char in alphabetCapital:
            position = alphabetCapital.find(char)
            newPosition = (position + key) % 26
            newChar = alphabetCapital[newPosition]
            encryption += newChar
        elif char not in alphabet or char not in alphabetCapital:
            encryption += char
    
    print(encryption)
        

encrypt()
