N = int(input(''))
for i in range(N):
    X, Y = map(int, input().split())
    Z = (X * Y) // 2
    print(Z, 'cm2')