linea = str(input())
splita = linea.split()
A = float(splita[0])
B = float(splita[1])
C = float(splita[2])
X = (B ** 2) - 4 * A * C
Y = 2 * A
if A == 0:
    print('Impossivel calcular')
elif X < 0:
    print('Impossivel calcular')
else:
    R1 = ((-B) + (X ** 0.5)) / Y
    R2 = ((-B) - (X ** 0.5)) / Y
    print('R1 = %0.5f' %R1)
    print('R2 = %0.5f' %R2)