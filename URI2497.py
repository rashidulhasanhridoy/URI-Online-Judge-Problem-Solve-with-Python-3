i = 1
while True:
    X = int(input(''))
    if X == -1:
        break
    else:
        print('Experiment %d: %d full cycle(s)' %(i, X // 2))
        i = i + 1
