def convertStrToInt(nro):
    if nro == '0':
        return 0
    if nro[0] == '-':
        signo = -1
        nro = nro[1:]
    else:
        signo = 1
    dicInt = {'0':0, '1':1, '2':2, '3':3, '4':4, '5':5, '6':6, '7':7, '8':8, '9':9}
    nroFinal = 0
    for i in range(0, len(nro)):
        nroFinal = nroFinal*10+dicInt[nro[i]]
    return nroFinal*signo

for i in range (-10000, 10000):
    assert convertStrToInt(str(i)) == i

assert convertStrToInt(str(1231)) == 1231





