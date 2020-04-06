Even = []
Odd = []
N = int(input(''))
for i in range(N):
    X = int(input(''))
    if X % 2 == 0:
        Even.append(X)
    else:
        Odd.append(X)
Even.sort()
Odd.sort()
Odd.reverse()
Numbers = Even + Odd
for i in range(N):
    print(Numbers[i], sep = '', end = '\n')