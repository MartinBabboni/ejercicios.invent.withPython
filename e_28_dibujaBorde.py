def drawBorder(ancho, alto):
    if ancho < 2 or alto <2:
        return
    print ('+'+'-'*(ancho-2)+'+')
    for linea in range(alto-2):
        print('|'+' '*(ancho-2)+'|')
    print ('+'+'-'*(ancho-2)+'+')

drawBorder(1, 3)
drawBorder(2, 2)
drawBorder(3, 3)
drawBorder(6, 3)
drawBorder(16, 4)
