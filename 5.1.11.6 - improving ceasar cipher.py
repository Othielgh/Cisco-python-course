# Scenario

# You are already familiar with the Caesar cipher, and this is why we want you to improve the code we showed you recently.

# The original Caesar cipher shifts each character by one: a becomes b, z becomes a, and so on. Let's make it a bit harder, and allow the shifted value to come from the range 1..25 inclusive.

# Moreover, let the code preserve the letters' case (lower-case letters will remain lower-case) and all non-alphabetical characters should remain untouched.

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


# what to do :

#     Calculate the position/index of the character in the 0-25 range.
#     Perform the positive shift using the modulo operation.
#     Find the character at the new position.
#     Replace the current capital letter by this new character.


# Caesar cipher - decrypting a message
#cipher = input('Enter your cryptogram: ')
import string

encryption = ''
alphabet = string.ascii_lowercase
alphabetCapital = string.ascii_uppercase


def encrypt():
    message = input("Enter the message you would like to encrypt: ")
    print()

    encryption = ''
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
            
    
    for char in message:
        if char in alphabet:
            position = alphabet.find(char)
            newPosition = (position + key) % 26
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
