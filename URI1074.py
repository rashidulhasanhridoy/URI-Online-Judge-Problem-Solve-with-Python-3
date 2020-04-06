N = int(input(''))
Numbers = []
for i in range(N):
    X = int(input(''))
    Numbers.insert(i, X)
for i in Numbers:
    if i == 0:
        print('NULL')
    elif i > 0:
        if i % 2 == 0:
            print('EVEN POSITIVE')
        else:
            print('ODD POSITIVE')
    elif i < 0:
        if i % 2 == 0:
            print('EVEN NEGATIVE')
        else:
            print('ODD NEGATIVE')