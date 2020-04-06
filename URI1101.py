sum = 0
while True:
    X, Y = map(int, input().split())
    if X == 0 or X < 0 or Y == 0 or Y < 0:
        break;
    elif X < Y:
        for i in range(X, Y + 1):
             sum += i
             print(i, end = ' ')
        print('Sum=', sum, sep = '')
        sum = 0
    else:
        for i in range(Y, X + 1):
             sum += i
             print(i, end=' ')
        print('Sum=', sum, sep = '')
        sum = 0