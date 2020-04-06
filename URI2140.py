bills = [7, 12, 22, 52, 102, 15, 25, 55, 105, 30, 60, 110, 70, 120, 150]
count = 0
while True:
    N, M = map(int, input().split())
    if N == 0 and M == 0:
        break
    for i in bills:
        if M - N == i:
            count = 1
            break
        else:
            count = 0
    if count == 1:
        print('possible')
    else:
        print('impossible')


