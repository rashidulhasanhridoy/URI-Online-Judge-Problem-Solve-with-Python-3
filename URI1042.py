linea = str(input())
splita = linea.split()
X = int(splita[0])
Y = int(splita[1])
Z = int(splita[2])
Numbers = [X, Y, Z]
for i in sorted(Numbers):
    print(i, sep = '\n')
print('', sep = '\n')
for i in Numbers:
    print(i, sep = '\n')