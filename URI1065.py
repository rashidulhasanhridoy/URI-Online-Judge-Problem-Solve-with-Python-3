A = int(input(''))
B = int(input(''))
C = int(input(''))
D = int(input(''))
E = int(input(''))
Numbers = [A, B, C, D, E]
count = 0
for i in Numbers:
    if i % 2 == 0:
        count += 1
print(count, 'valores pares')