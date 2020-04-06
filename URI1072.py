N = int(input(''))
Numbers = []
for i in range(N):
    X = int(input(''))
    Numbers.insert(i, X)
tin = 0
tout = 0
for i in Numbers:
    if i >= 10 and i <= 20:
        tin += 1
    else:
        tout += 1
print(tin, 'in')
print(tout, 'out')

