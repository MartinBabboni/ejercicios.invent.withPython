import random
def generatePassword(nro):
    if nro < 12:
        nro =12
    passWord = []
    passWord.append(chr(random.randint(48, 57)))
    passWord.append(chr(random.randint(65, 90)))
    passWord.append(chr(random.randint(97, 120)))
    especial = ['~','!','@','#','$','%','^','&','*','(',')','_','+']
    passWord.append(especial[random.randint(0,12)])
    while len(passWord) < nro:
        clave = random.randint(0, 3)
        if clave ==0:
            passWord.append(chr(random.randint(48, 57)))
        elif clave ==1:
            passWord.append(chr(random.randint(65, 90)))
        elif clave ==2:
            passWord.append(chr(random.randint(97, 120)))
        else:
            passWord.append(especial[random.randint(0,12)])
    random.shuffle(passWord)
    return ''.join(passWord)

LOWER_LETTERS = 'abcdefghijklmnopqrstuvwxyz'
UPPER_LETTERS = 'ABCDEFGHIJKLMNOPQRSTUVWXYZ'
NUMBERS = '1234567890'
SPECIAL = '~!@#$%^&*()_+'
pw = generatePassword(14)
assert len(pw) == 14
hasLowercase = False
hasUppercase = False
hasNumber = False
hasSpecial = False
for character in pw:
    if character in LOWER_LETTERS:
        hasLowercase = True
    if character in UPPER_LETTERS:
        hasUppercase = True
    if character in NUMBERS:
        hasNumber = True
    if character in SPECIAL:
        hasSpecial = True
assert hasLowercase and hasUppercase and hasNumber and hasSpecial
