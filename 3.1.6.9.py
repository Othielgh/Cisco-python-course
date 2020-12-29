myList = [1, 2, 4, 4, 1, 4, 2, 6, 2, 9]
myList2 = []

for number in myList:
    if number in myList2:
        continue
    else:
        myList2.append(number)

print("The list with unique elements only:")
print(myList2)