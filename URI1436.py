N = int(input(''))
for i in range(1, N + 1):
    X = list(map(int, input('').split()))
    A = X[0]
    B = X[1:]
    B.sort()
    Y = (A // 2) + 1
    print('Case %d: %d' %(i, B[-Y]))