sum = 0
C = int(input(''))
for i in range(C):
    X = int(input(''))
    for i in range(1, X + 1):
        if i % 2 != 0:
            sum = sum + 1
        else:
            sum = sum - 1
    print(sum)
    sum = 0