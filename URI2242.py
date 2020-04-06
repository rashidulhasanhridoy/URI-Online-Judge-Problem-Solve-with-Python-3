S = str(input(''))
T = ''
V = ['a', 'e', 'i', 'o', 'u']
for i in range(len(S)):
    if S[i] in V:
        T += S[i]
if T == T[::-1]:
    print('S')
else:
    print('N')