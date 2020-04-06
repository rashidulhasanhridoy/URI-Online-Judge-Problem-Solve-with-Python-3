N = int(input(''))
for i in range(N):
    X = str(input(''))
    if len(X) == 5:
        print('3')
    elif (X[0] == 'o' and X[1] == 'n') or (X[0] == 'o' and X[2] == 'e') or (X[1] == 'n' and X[2] == 'e'):
        print('1')
    else:
        print('2')