X = list(map(float, input().split()))
Xmax = max(X)
Xmin = min(X)
Xt = 0
for i in X:
    Xt += i
Y = Xt - Xmax - Xmin
print('%0.1f' %Y)