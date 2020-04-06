A = str(input(''))
for i in A:
    if i == '.':
        break
C = A.index(i)
B = int(A[:C])
E = A[C]
D = int(A[C + 1 : len(A)])
print(D, E,  B, sep = '')