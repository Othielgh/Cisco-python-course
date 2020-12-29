def isYearLeap(year):
    if year < 1538:
        print('Not gregorian')
        return False
    elif year % 4 != 0:
        print('Not a Leap year')
        return False
    elif year % 100 == 0 and year % 400 == 0:
        print('This is a centurial leap year')
        return True
    elif year % 100 == 0 and year % 400 != 0:
        print('This is a regular centurial leap year')
        return False
    else:
        print('This is a leap year!')
        return True
        

testData = [1900, 2000, 2016, 1987]
testResults = [False, True, True, False]
for i in range(len(testData)):
	yr = testData[i]
	print(yr,"->",end="")
	result = isYearLeap(yr)
	if result == testResults[i]:
		print("OK")
	else:
		print("Failed")