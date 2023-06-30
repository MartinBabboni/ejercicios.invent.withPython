"""def drawPyramid(altura):
    if altura <1:
        return
    caracteres = 1
    for alto in range (altura):
        print (('#'*caracteres).center((altura*2)-1))
        caracteres +=2"""

def drawPyramid(altura):
    for alto in range(altura):
        espacioalaIzquierda=' '*(altura-(alto+1))
        anchoPiramide= '#'*(alto*2+1)
        print(espacioalaIzquierda+anchoPiramide)


drawPyramid(1)
drawPyramid(2)
drawPyramid(3)
drawPyramid(5)
drawPyramid(8)
drawPyramid(19)
