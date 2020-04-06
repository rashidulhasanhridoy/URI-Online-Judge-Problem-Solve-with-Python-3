A = float(input(''))
B = float(input(''))
C = float(input(''))
D = float(input(''))
E = float(input(''))
F = float(input(''))
Numbers = [A, B, C, D, E, F]
count = 0
for i in Numbers:
    if i > 0:
        count += 1
print(count, 'valores positivos')
