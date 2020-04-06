N = int(input(''))
for i in range(N):
    X, Y = map(int, input().split())
    R = ((3 * X) ** 2) + (Y ** 2)
    B = (2 * (X ** 2)) + ((5 * Y) ** 2)
    C = ((-100) * X) + (Y ** 3)
    Numbers = [R, B, C]
    Z = max(Numbers)
    if Z == Numbers[0]:
        print('Rafael ganhou')
    elif Z == Numbers[1]:
        print('Beto ganhou')
    elif Z == Numbers[2]:
        print('Carlos ganhou')