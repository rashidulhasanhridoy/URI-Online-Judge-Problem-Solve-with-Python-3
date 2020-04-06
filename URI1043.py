linea = str(input(''))
splita = linea.split()
A = float(splita[0])
B = float(splita[1])
C = float(splita[2])
if C < A + B and B < A + C and A < B + C:
    Perimetro = A + B + C
    print('Perimetro = %0.1f' %Perimetro)
else:
    Area = ((A + B) / 2) * C
    print('Area = %0.1f' %Area)