# Some say that the Digit of Life is a digit evaluated using somebody's birthday. It's simple - you just need to sum all the digits of the date. If the result contains more than one digit, you have to repeat the addition until you get exactly one digit. For example:

#     1 January 2017 = 2017 01 01
#     2 + 0 + 1 + 7 + 0 + 1 + 0 + 1 = 12
#     1 + 2 = 3

# 3 is the digit we searched for and found.

# Your task is to write a program which:

#     asks the user her/his birthday (in the format YYYYMMDD, or YYYYDDMM, or MMDDYYYY - actually, the order of the digits doesn't matter)
#     outputs the Digit of Life for the date.

def digitOfLife(date):
    date = str(date)
    # Remove unwanted characters
    for char in ' ?-.!/;:':
        date = date.replace(char,'')
    if len(date) < 2:
        print(date)
        return int(date)
    else:
        print(date) # Shows the steps it takes
        return digitOfLife(sum([int(d) for d in str(date)]))
    
    

digitOfLife(input('Please enter your date of birth(DD/MM/YYYY): '))