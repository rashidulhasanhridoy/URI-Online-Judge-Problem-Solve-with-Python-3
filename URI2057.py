S, T, F = map(int, input().split())
X = S + T + F
if X == 24:
    Y = 0
elif X > 24:
    Y = X - 24
elif X < 0:
    Y = X + 24
else:
    Y = X
print(Y)


