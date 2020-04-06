X = int(input())
Y = int(input())
sum = 0
if X < Y:
    for i in range(X, Y + 1):
        if i % 13 != 0:
            sum += i
    print(sum)
elif Y < X:
    for i in range(Y, X + 1):
        if i % 13 != 0:
            sum += i
    print(sum)