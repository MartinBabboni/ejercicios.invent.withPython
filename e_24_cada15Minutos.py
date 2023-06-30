"""for a in range (1, 3):
    for b in range (0, 12):
        for c in range (0, 59, 15):
            if a == 1:
                dia = 'am'
            else:
                dia = 'pm'
            if b== 0:
                hora = '12'
            else:
                hora = str(b)
            if c==0:
                minuto = '00'
            else:
                minuto = str(c)
            print (f"{hora}:{minuto} {dia}")"""

# Otra alternativa
for a in ['am', 'pm']:
    for b in ['12','01','02','03','04','05','06','07','08','09','10','11']:
        for c in ['00','15','30','45']:
            print (f"{b}:{c} {a}")


