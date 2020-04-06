while True:
    H1, M1, H2, M2 = map(int, input().split())
    if H1 == 0 and M1 == 0 and H2 == 0 and M2 == 0:
        break
    else:
        if H1 == H2:
            if M1 < M2:
                M = M2 - M1
                print(M)
            else:
                H = 24 - H1 + H2 - 1
                M = (H * 60) + 60 - M1 + M2
                print(M)
        elif H1 > H2:
            H = 24 - H1 + H2 - 1
            M = (H * 60) + 60 - M1 + M2
            print(M)
        elif H1 < H2:
            H = H2 - H1 - 1
            M = (H * 60) + 60 - M1 + M2
            print(M)