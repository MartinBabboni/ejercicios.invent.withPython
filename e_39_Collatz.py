def collatz(nro):
    collatzList = []
    if nro < 1:
        return collatzList
    #if nro == 1:
    #    collatzList = [1]
    while nro >= 1:
        collatzList.append(int(nro))
        if nro == 1:
            return collatzList
        if nro%2 == 0:
            nro = nro/2
        else:
            nro = (nro*3)+1


assert collatz(0) == []
assert collatz(10) == [10, 5, 16, 8, 4, 2, 1]
assert collatz(11) == [11, 34, 17, 52, 26, 13, 40, 20, 10, 5, 16, 8, 4, 2, 1]
assert collatz(12) == [12, 6, 3, 10, 5, 16, 8, 4, 2, 1]
assert len(collatz(256)) == 9
assert len(collatz(257)) == 123
import random
random.seed(42)
for i in range(1000):
    startingNum = random.randint(1, 10000)
    seq = collatz(startingNum)
    assert seq[0] == startingNum # Make sure it includes the starting number.
    assert seq[-1] == 1 # Make sure the last integer is 1.