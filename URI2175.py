O, B, I = map(float, input().split())
if (O == B) or (B == I) or (I == O) or (O == B and B == I):
    print('Empate')
else:
    Numbers = [O, B, I]
    X = min(Numbers)
    if X == Numbers[0]:
        print('Otavio')
    elif X == Numbers[1]:
        print('Bruno')
    elif X == Numbers[2]:
        print('Ian')