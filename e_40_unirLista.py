def mergeTwoLists(lista1, lista2):
    listafinal = []
    i1 = 0
    i2 = 0
    while i1 < len(lista1) and i2 < len(lista2):
        if lista1[i1] < lista2[i2]:
            listafinal.append(lista1[i1])
            i1 += 1             
        else:
            listafinal.append(lista2[i2])
            i2 +=1
            

    if i1 < len(lista1):    
        for a in range (i1, len(lista1)):
            listafinal.append(lista1[a])
    if i2 < len(lista2):
                for a in range (i2, len(lista2)):
                    listafinal.append(lista2[a])
    return listafinal

print(mergeTwoLists([4, 5], [1, 2, 3]))

