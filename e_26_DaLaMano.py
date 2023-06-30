def printHandshakes(lista):
    manosDadas = 0
    paso = 1
    for persona in range (0, (len(lista)-1)):
        for siguientepersona in range (paso, len(lista)):
            print (f"{lista[persona]} shakes hands with {lista[siguientepersona]}")
            manosDadas +=1
        paso +=1
    return manosDadas


assert printHandshakes(['Alice', 'Bob']) == 1
assert printHandshakes(['Alice', 'Bob', 'Carol']) == 3
assert printHandshakes(['Alice', 'Bob', 'Carol', 'David']) == 6
