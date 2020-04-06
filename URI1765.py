while True:
    T = int(input(''))
    if T == 0:
        break
    else:
        for i in range(T):
            X = str(input(''))
            S = X.split()
            C = int(S[0])
            A = float(S[1])
            B = float(S[2])
            D = (((A + B) / 2) * 5) * C
            print('Size #%d:' %(i+1))
            print('Ice Cream Used: %0.2f cm2' %D)
        print('', end = '\n')
