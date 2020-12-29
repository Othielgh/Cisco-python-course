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
        

def daysInMonth(year, month):
    numDaysInMonth = [31, 28, 31, 30, 31, 30, 31, 31, 30, 31, 30 ,31]
    
    if isYearLeap(year) and month == 2:
        return 29
    else:
        return numDaysInMonth[month -1]  # month -1 because the index position of list starts at 0 and months count from 1

testYears = [1900, 2000, 2016, 1987]
testMonths = [2, 2, 1, 11]
testResults = [28, 29, 31, 30]
for i in range(len(testYears)):
	yr = testYears[i]
	mo = testMonths[i]
	print(yr, mo, "->", end="")
	result = daysInMonth(yr, mo)
	if result == testResults[i]:
		print("OK")
	else:
		print("Failed")