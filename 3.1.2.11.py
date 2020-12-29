wordWithoutVovels = ""

userWord = input("Please input any word: ")
userWord = userWord.upper()

for letter in userWord:
    if letter == 'A':
        continue
    elif letter == 'E':
        continue
    elif letter == 'I':
        continue
    elif letter == 'O':
        continue
    elif letter == 'U':
        continue
    else:
        wordWithoutVovels = wordWithoutVovels + letter

print(wordWithoutVovels)
    # Complete the body of the loop.

# Print the word assigned to wordWithoutVowels.