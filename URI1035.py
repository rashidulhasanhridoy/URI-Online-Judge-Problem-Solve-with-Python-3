linea = str(input(''))
splita = linea.split()
A = int(splita[0])
B = int(splita[1])
C = int(splita[2])
D = int(splita[3])
if B > C and D > A and (C + D) > (A + B) and C > 0 and D > 0 and A % 2 == 0:
    print('Valores aceitos')
else:
    print('Valores nao aceitos')