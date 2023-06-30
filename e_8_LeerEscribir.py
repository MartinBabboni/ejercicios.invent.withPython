def writeToFile(archivo, texto):
    archivo = open(f"/home/martin/Documentos/Python/GuiaDeEjercicios/{archivo}", 'w')
    archivo.write(texto)
    archivo.close()

def appendToFile(archivo, texto):
    archivo = open(f"/home/martin/Documentos/Python/GuiaDeEjercicios/{archivo}", 'a')
    archivo.write(texto)
    archivo.close()

def readFromFile(archivo):
    archivo = open(f"/home/martin/Documentos/Python/GuiaDeEjercicios/{archivo}", 'r')
    return archivo.read()

writeToFile('greet.txt', 'Hello!\n')
appendToFile('greet.txt', 'Goodbye!\n')
assert readFromFile('greet.txt') == 'Hello!\nGoodbye!\n'
