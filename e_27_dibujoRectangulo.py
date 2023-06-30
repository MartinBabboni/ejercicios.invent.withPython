def drawRectangle(ancho, alto):
    if ancho < 1 or alto <1:
        return
    for linea in range(alto):
        for caracter in range (ancho):
            print('#', end='')
        print()

"""def drawRectangle(ancho, alto):
    for linea in range(alto):
        print('#'*ancho)"""

drawRectangle(10, 4)
drawRectangle(10, 0)
drawRectangle(0, 10)
