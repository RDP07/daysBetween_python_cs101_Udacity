#counts days inbetween birth ro current day taking into account leap years.
    
def nextDay(year, month, day):
    """
    Returns the year, month, day of the next day.
    Simple version: assume every month has 30 days.
    """
    if day < 30:
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