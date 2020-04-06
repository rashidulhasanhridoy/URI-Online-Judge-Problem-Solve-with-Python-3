linea = str(input(''))
splita = linea.split()
A = int(splita[0])
B = int(splita[1])
C = int(splita[2])
large = 0
numbers = [A, B, C]
for i in numbers:
    if i > large:
        large = i
print(large, 'eh o maior')