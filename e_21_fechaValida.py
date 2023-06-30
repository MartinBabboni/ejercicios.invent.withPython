from e_20_biciesto import isLeapYear
def isValidDate(anio, mes, dia):
    if isLeapYear(anio):
        febrero = 29
    else:
        febrero = 28
    #mesLargo=[1,3,5,7,8,10,12]
    mesCorto=[4,6,9,11]
    if mes>12 or mes< 1 or dia <1 or dia>31:
        return False
    if mes in mesCorto and dia>30:
        return False
    if mes==2 and dia>febrero:
        return False
    return True

assert isValidDate(1999, 12, 31) == True
assert isValidDate(2000, 2, 29) == True
assert isValidDate(2001, 2, 29) == False
assert isValidDate(2029, 13, 1) == False
assert isValidDate(1000000, 1, 1) == True
assert isValidDate(2015, 4, 31) == False
assert isValidDate(1970, 5, 99) == False
assert isValidDate(1981, 0, 3) == False
assert isValidDate(1666, 4, 0) == False
import datetime
d = datetime.date(1970, 1, 1)
oneDay = datetime.timedelta(days=1)

for i in range(1000000):
    assert isValidDate(d.year, d.month, d.day) == True
    d += oneDay
