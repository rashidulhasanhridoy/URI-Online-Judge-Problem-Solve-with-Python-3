while True:
    M, N = map(int, input('').split())
    if M == 0 and N == 0:
        break
    else:
        O = M + N
        P = str(O)
        print(P.replace('0', ''))