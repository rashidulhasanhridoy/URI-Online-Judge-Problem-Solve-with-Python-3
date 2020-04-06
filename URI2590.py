T = int(input(''))
for i in range(T):
    N = int(input(''))
    if N % 4 == 0:
        print('1')
    elif N % 4 == 1:
        print('7')
    elif N % 4 == 2:
        print('9')
    elif N % 4 == 3:
        print('3')