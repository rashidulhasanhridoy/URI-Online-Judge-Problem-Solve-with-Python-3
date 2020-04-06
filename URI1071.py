X = int(input(''))
Y = int(input(''))
odd = 0
if X == Y:
    odd = 0
elif X < Y:
    for i in range(X + 1, Y):
        if i % 2 != 0:
            odd += i
else:
    for i in range(Y + 1, X):
        if i % 2 != 0:
            odd += i
print(odd)