Q, e = map(int, input().split())
E = list(map(int, input().split()))
count = 0
for i in range(Q):
    X = int(input(''))
    for i in E:
        if i == X:
            count = 1
            break
        else:
           count = 0
    if count == 1:
        print('0')
        count = 0
    else:
        print('1')
        E.append(X)
        count = 0
