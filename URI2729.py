Names = []
N = int(input(''))
for i in range(N):
    X = list(map(str, input('').split()))
    for j in X:
        if j not in Names:
            Names.append(j)
    Names.sort()
    for k in range(len(Names)):
        print(Names[k], end = '')
        if k == len(Names) - 1:
            break
        print(' ', end = '')
    print('')
    Names = []