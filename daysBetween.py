#counts days inbetween birth ro current day taking into account leap years.
 
 def isLeapYear(year):
    """Procedure to define when leapyear occured"""
    if year % 400 == 0:
        return True
    if year % 100 == 0:
        return False
    if year % 4 == 0: 
        return True
    return False

def daysInMonth(year, month):
    """Correct version with correct days in each month and accounting for leap years."""
    if month == 1 or month == 3 or month == 5 or month == 7 or month == 8 or month == 10 or month == 12:
        return 31
    else:
        if month == 2:
            if isLeapYear(year):
                return 29
            return 28
        else:
            return 30  

def nextDay(year, month, day):
    """
    Returns the year, month, day of the next day.
    Simple version: assume every month has 30 days.
    """
    if day < daysInMonth(year, month):
        return year, month, day + 1
    else:
        if month < 12:
            return year, month + 1, 1
        else:
            return year + 1, 1, 1

print nextDay(2012, 2, 30) 

def dateIsBefore(year1, month1, day1, year2, month2, day2):
    """helper procedure for what will be daysBetweenDates()"""
    if year1 < year2:
        return True
    if year1 == year2:
        if month1 < month2:
            return True
        if month1 == month2:
            return day1 < day2
    return False

def daysBetweenDates(year1, month1, day1, year2, month2, day2):
    """Returns the number of days between year1/month1/day1
       and year2/month2/day2. Assumes inputs are valid dates
       in Gregorian calendar, and the first date is not after
       the second."""
    assert not dateIsBefore(year2, month2, day2, year1, month1, day1)
    days = 0
    while dateIsBefore(year1, month1, day1, year2, month2, day2):
        year1, month1, day1 = nextDay(year1, month1, day1)
        days += 1
    return days