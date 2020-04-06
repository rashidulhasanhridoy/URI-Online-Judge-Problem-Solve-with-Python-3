QT = int(input(''))
for i in range(QT):
    A, X, B, Y = map(str, input().split())
    M, N = map(int, input().split())
    if (M + N) % 2 == 0:
        if X[0] == 'P':
            print(A)
        else:
            print(B)
    else:
        if X[0] == 'I':
            print(A)
        else:
            print(B)