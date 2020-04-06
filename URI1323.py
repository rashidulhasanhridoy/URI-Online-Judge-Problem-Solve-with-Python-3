while True:
    N = int(input(''))
    if N == 0:
        break
    else:
        print('%d' %((N*(N+1)*((2*N)+1))/6))