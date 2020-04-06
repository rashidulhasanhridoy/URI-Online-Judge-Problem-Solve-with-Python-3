N = int(input(''))
for i in range(N):
    X, Y = map(int, input().split())
    if Y == 0:
        print('divisao impossivel')
    else:
        result = X / Y
        print('%0.1f' %result)
