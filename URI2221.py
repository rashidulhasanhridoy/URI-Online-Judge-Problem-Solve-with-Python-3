T = int(input(''))
X = 0
Y = 0
for i in range(T):
    B = int(input(''))
    A1, D1, L1 = map(int, input().split())
    A2, D2, L2 = map(int, input().split())
    X = (A1 + D1) / 2
    if L1 % 2 == 0:
        X = X + L1
    Y = (A2 + D2) / 2
    if L2 % 2 == 0:
        Y = Y + L1
    if X == Y:
        print('Empate')
    elif X > Y:
        print('Dabriel')
    else:
        print('Guarte')

