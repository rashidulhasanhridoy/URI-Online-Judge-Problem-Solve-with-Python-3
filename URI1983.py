regNumber = []
Score = []
large = 0
N = int(input(''))
for i in range(N):
    linea = str(input(''))
    splita = linea.split()
    X = int(splita[0])
    regNumber.append(X)
    Y = float(splita[1])
    Score.append(Y)
for i in Score:
    if i > large:
        large = i
if large < 8.0:
    print('Minimum note not reached')
else:
    position = Score.index(large)
    print(regNumber[position])
