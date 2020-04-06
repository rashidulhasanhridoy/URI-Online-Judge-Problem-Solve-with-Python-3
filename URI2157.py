def MirrorSequence(a, b):
    s = ''
    for i in range(a, b+1):
        s += str(i)
    return s + s[::-1]

C = int(input(''))
for i in range(C):
    E, B = map(int, input().split())
    print(MirrorSequence(E, B))
