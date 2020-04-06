sum = 0
N = int(input(''))
for i in range(N):
    X, Y = map(int, input().split())
    if X == 1001:
        sum = sum + (Y * 1.50)
    elif X == 1002:
        sum = sum + (Y * 2.50)
    elif X == 1003:
        sum = sum + (Y * 3.50)
    elif X == 1004:
        sum = sum + (Y * 4.50)
    elif X == 1005:
        sum = sum + (Y * 5.50)
print('%0.2f' %sum)