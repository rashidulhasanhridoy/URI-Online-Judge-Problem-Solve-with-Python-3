linea = str(input(''))
splita = linea.split()
X = float(splita[0])
Y = float(splita[1])
Z = float(splita[2])
ANumbers = [X, Y, Z]
Numbers = sorted(ANumbers)
A = Numbers[2]
B = Numbers[1]
C = Numbers[0]
if A >= B + C:
    print('NAO FORMA TRIANGULO')
else:
    if (A ** 2) == ((B ** 2) + (C ** 2)):
        print('TRIANGULO RETANGULO')
    if (A ** 2) > ((B ** 2) + (C ** 2)):
        print('TRIANGULO OBTUSANGULO')
    if (A ** 2) < ((B ** 2) + (C ** 2)):
        print('TRIANGULO ACUTANGULO')
    if A == B and B == C and C == A:
        print('TRIANGULO EQUILATERO')
    if (A == B and B != C) or (B == C and C != A) or (C == A and C != B):
        print('TRIANGULO ISOSCELES')