def rot13(texto):
    nuevotexto =''
    for letra in range (len(texto)):
        if texto[letra].isalpha():
            b = ord(texto[letra])
            if texto[letra].isupper():
                if b < 78:
                    nuevotexto += chr(b+13)
                else:
                    nuevotexto += chr(b-13)
            else:
                if b < 110:
                    nuevotexto += chr(b+13)
                else:
                    nuevotexto += chr(b-13)
        else:
            nuevotexto += texto[letra]
    return nuevotexto

assert rot13('Hello, world!') == 'Uryyb, jbeyq!'
assert rot13('Uryyb, jbeyq!') == 'Hello, world!'
assert rot13(rot13('Hello, world!')) == 'Hello, world!'
assert rot13('abcdefghijklmnopqrstuvwxyz') == 'nopqrstuvwxyzabcdefghijklm'
assert rot13('ABCDEFGHIJKLMNOPQRSTUVWXYZ') == 'NOPQRSTUVWXYZABCDEFGHIJKLM'