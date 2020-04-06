sum = 0
while True:
    L, R = map(int, input().split())
    if L == 0 and R == 0:
        break
    sum = L + R
    print(sum)
    sum = 0