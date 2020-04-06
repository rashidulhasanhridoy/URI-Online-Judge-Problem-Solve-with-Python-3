N = int(input(''))
A, B = map(int, input().split())
C = A + B
if C == N or C < N:
    print('Farei hoje!')
else:
    print('Deixa para amanha!')