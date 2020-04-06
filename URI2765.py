C = 0
X = str(input(''))
for i in X:
    if i == ',':
        C = X.index(i)
        break
print(X[:C])
print(X[C+1 : len(X)])