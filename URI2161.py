def squareRootofTen(n):
    X = 3.0
    if n == 0:
        return X
    else:
        return X + squareRootofTenA(n)
def squareRootofTenA(n):
    if n == 0:
        return 0
    else:
        Y = 6 + squareRootofTenA(n - 1)
        return(1 / Y)
N = int(input(''))
print('%0.10f' %(squareRootofTen(N)))