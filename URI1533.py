while True:
    N = int(input(''))
    if N == 0:
        break
    else:
        V = list(map(int, input().split()))
        X = sorted(V)
        for i in V:
            if i == X[-2]:
                Y = V.index(i) + 1
                print(Y)
