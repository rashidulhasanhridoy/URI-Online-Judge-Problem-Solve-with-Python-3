N = int(input(''))
for i in range(N):
    X = int(input(''))
    if X > 2015:
        year = X - 2015 + 1
        print(year, 'A.C.')
    elif X < 2015:
        year = 2015 - X
        print(year, 'D.C.')
    elif X == 2015:
        print('1 A.C.')
