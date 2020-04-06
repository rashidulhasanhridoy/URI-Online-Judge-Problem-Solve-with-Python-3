A, B, C = map(int, input().split())
Numbers = [A, B, C]
X = max(Numbers)
Y = min(Numbers)
Z = A + B + C - X - Y
if X >= Y + Z:
    print('Invalido')
else:
    if A != B and B != C and C != A:
        print('Valido-Escaleno')
        if A * A == B *B + C * C:
            print('Retangulo: S')
        else:
            print('Retangulo: N')
    elif A == B and B == C and C == A:
        print('Valido-Equilatero')
        if A * A == B *B + C * C:
            print('Retangulo: S')
        else:
            print('Retangulo: N')
    elif (A == B and B != C) or (B == C and C != A) or (C == A and A != B):
        print('Valido-Isoceles')
        if A * A == B *B + C * C:
            print('Retangulo: S')
        else:
            print('Retangulo: N')