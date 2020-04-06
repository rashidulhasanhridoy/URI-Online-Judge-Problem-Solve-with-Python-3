N = int(input(''))
for i in range(N):
    X, Y = map(int, input().split('x'))
    if X == Y:
        for j in range(5, 11, 1):
            print(X, 'x', j, '=', '%d' %(X * j))
    else:
        for j in range(5, 11, 1):
            print(X, 'x', j, '=', '%d' %(X * j), '&&', Y, 'x', j, '=', '%d' %(Y * j))