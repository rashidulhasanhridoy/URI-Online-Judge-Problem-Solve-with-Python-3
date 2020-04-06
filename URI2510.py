N = int(input(''))
for i in range(N):
    X = str(input(''))
    length = len(X)
    if length > 0 and length <= 25:
        print('Y')
    else:
        print('N')
