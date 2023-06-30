def mode(lista):
    if len(lista) ==0:
        return None
    dic = {}
    for nro in lista:
        if nro not in dic:
            dic.setdefault(nro, 1)
        else:
            dic[nro] +=1
    modo=''
    rep=0
    for k, v in dic.items():
        if v > rep:
            rep=v
            modo=k
    return modo



assert mode([]) == None
assert mode([1, 2, 3, 4, 4]) == 4
assert mode([1, 1, 2, 3, 4]) == 1
import random
random.seed(42)
testData = [1, 2, 3, 4, 4]
for i in range(1000):
    random.shuffle(testData)
    assert mode(testData) == 4
