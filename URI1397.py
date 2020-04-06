Xt = 0
Yt = 0
while True:
    N = int(input(''))
    if N == 0:
        break
    else:
        for i in range(N):
            X, Y = map(int, input('').split())
            if X > Y:
                Xt += 1
            elif X < Y:
                Yt += 1
        print('%d %d' %(Xt, Yt))
        Xt = 0
        Yt = 0