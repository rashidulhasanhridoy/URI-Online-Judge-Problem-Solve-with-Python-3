sum = 0
N = int(input(''))
for i in range(N):
    X, Y = map(int, input().split())
    sum = X + Y
    print(sum)
    sum = 0