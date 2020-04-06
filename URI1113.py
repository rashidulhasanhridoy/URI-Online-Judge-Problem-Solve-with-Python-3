while True:
    X, Y = map(int, input().split())
    if X == Y:
        break;
    elif X < Y:
        print('Crescente')
    else:
        print('Decrescente')
