A0 = 0
A1 = 0
N = int(input())
X = list(map(int, input().split()))
for i in X:
    if i == 0:
        A0 += 1
    elif i == 1:
        A1 += 1
if A0 > A1:
    print('Y')
elif A0 < A1:
    print('N')
elif A0 == A1:
    print('N')