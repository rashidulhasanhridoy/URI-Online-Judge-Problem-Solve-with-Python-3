N = int(input(''))
odd = 0
for i in range(N):
    X, Y = map(int, input().split())
    if X < Y:
        for i in range(X + 1, Y):
            if i % 2 != 0:
                odd += i
        print(odd)
        odd = 0
    else:
        for i in range(Y + 1, X):
            if i % 2 != 0:
                odd += i
        print(odd)
        odd = 0