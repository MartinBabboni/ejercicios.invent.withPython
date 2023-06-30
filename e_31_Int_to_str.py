def convertIntToStr(nro):
    if nro == 0:
        return '0'
    if nro < 0:
        signo = '-'
    else:
        signo = ''
    dicNros = {0:'0', 1:'1', 2:'2', 3:'3', 4:'4', 5:'5', 6:'6', 7:'7', 8:'8', 9:'9'}
    nroStr= ''
    nro = abs(nro)
    while nro > 0:
        nroStr = dicNros[nro%10] + nroStr
        nro = nro//10
    return signo + nroStr


for i in range (-10000, 1000):
    assert convertIntToStr(i) == str(i)