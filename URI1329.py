Mary = 0
John = 0
while True:
    N = int(input(''))
    if N == 0:
        break
    X = list(map(int, input().split()))
    for i in X:
        if i == 0:
            Mary += 1
        elif i == 1:
            John += 1
    print('Mary won %d times and John won %d times' %(Mary, John))
    Mary = 0
    John = 0

