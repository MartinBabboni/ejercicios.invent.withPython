def commaFormat(nro):
    nroStr = str(nro)
    if '.' in nroStr:
        indice = nroStr.index('.')
        enteros = nroStr[0:indice]
        decimales = nroStr[indice:]
    else:
        enteros = nroStr
        decimales = ''
    if '-' in enteros:
        signo = '-'
        enteros = enteros[1:]
    else:
        signo =''
    lista = []
    for a in range(1, len(enteros)+1):
        #print (a)
        lista.append(enteros[-a])
        #if a%3 == 0 and a != 0:
         #   lista.append(',')
        if a%3 == 0 and a != 0:
            lista.append(',')
    lista.reverse()
    if lista[0] == ',':
        lista = lista[1:]
    enteroConComa = ''.join(lista)  
    return signo+enteroConComa+decimales
    
assert commaFormat(1) == '1'
assert commaFormat(10) == '10'
assert commaFormat(100) == '100'
assert commaFormat(1000) == '1,000'
assert commaFormat(10000) == '10,000'
assert commaFormat(100000) == '100,000'
assert commaFormat(1000000) == '1,000,000'
assert commaFormat(1234567890) == '1,234,567,890'
assert commaFormat(1000.123456) == '1,000.123456'