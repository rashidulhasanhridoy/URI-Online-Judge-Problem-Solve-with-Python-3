N = int(input(''))
for i in range(N):
    linea = str(input())
    splita = linea.split()
    X = str(splita[0])
    Y = int(splita[1])
    if X == 'Thor':
        print('Y')
    else:
        print('N')