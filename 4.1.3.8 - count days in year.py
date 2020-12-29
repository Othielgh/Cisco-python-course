def isYearLeap(year):
    if year < 1538:
        return False
    elif year % 4 != 0:
        return False
    elif year % 100 == 0 and year % 400 == 0:
        return True
    elif year % 100 == 0 and year % 400 != 0:
        return False
    else:
        return True

def daysInMonth(year, month):
    numDaysInMonth = [31, 28, 31, 30, 31, 30, 31, 31, 30, 31, 30 ,31]
    
    if isYearLeap(year) and month == 2:
        return 29
    else:
        return numDaysInMonth[month -1]

def dayOfYear(year, month, day):
    
    if year < 1538 or month < 1 or month > 12:
        return None
    
    totalNumDays = day
    month -= 1  # remove 1 to get right place in list
    
    while month > 0:
        totalNumDays += daysInMonth(year, month)
        month -= 1
    
    return totalNumDays

print(dayOfYear(2000, 12, 31))