def isLeapYear(anio):
    if anio%400==0:
        return True
    elif anio%100==0:
        return False
    elif anio%4==0:
        return True
    else:
        return False



assert isLeapYear(1999) == False
assert isLeapYear(2000) == True
assert isLeapYear(2001) == False
assert isLeapYear(2004) == True
assert isLeapYear(2100) == False
assert isLeapYear(2400) == True
