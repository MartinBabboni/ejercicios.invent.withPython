print ("  |", end='')
for a in range(1, 11):
    print(str(a).rjust(3), end='')
print ()
print ('--+-------------------------------')
for a in range(1, 11):
    print ((str(a)+'|').rjust(3),end='')
    for b in range(1, 11):
        print (str(a*b).rjust(3), end='')
    print ()
