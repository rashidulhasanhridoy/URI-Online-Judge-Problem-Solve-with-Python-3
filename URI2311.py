sum = 0
N = int(input(''))
for i in range(N):
    name = str(input(''))
    D = float(input(''))
    S1, S2, S3, S4, S5, S6, S7 = map(float, input().split())
    S = [S1, S2, S3, S4, S5, S6, S7]
    for i in S:
        sum += i
    X = (sum - max(S) - min(S)) * D
    print(name, '%0.2f' %X)
    sum = 0
