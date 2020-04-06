A = int(input(''))
B = int(input(''))
C = int(input(''))
D = int(input(''))
E = int(input(''))
Numbers = [A, B, C, D, E]
even = 0
odd = 0
pos = 0
neg = 0
for i in Numbers:
    if i % 2 == 0:
        even += 1
    if i % 2 != 0:
        odd += 1
    if i > 0:
        pos += 1
    if i < 0:
        neg += 1
print(even, 'valor(es) par(es)')
print(odd, 'valor(es) impar(es)')
print(pos, 'valor(es) positivo(s)')
print(neg, 'valor(es) negativo(s)')