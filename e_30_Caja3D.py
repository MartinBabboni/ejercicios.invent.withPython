def drawBox(lado):
    print(('+'+'-'*(lado*2)+'+').rjust((lado*3)+3))
    for persp in range(lado):
        print(('/'+' '*(lado*2)+'/'+' '*persp+'|').rjust((lado*3)+3))
    print ('+'+'-'*(lado*2)+'+'+' '*lado+'+')
    for alto in range(lado):
        print('|'+' '*(lado*2)+'|'+' '*(lado-(alto+1))+'/')
    print ('+'+'-'*(lado*2)+'+')




drawBox(1)
drawBox(2)
drawBox(3)
drawBox(4)
drawBox(5)




