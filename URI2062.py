N = int(input(''))
X = input().split()
j = 0
for i in X:
    if j:
        print(' ', end = '')
    if i[:2] == 'OB' and len(i) == 3:
        print('OBI', end = '')
    elif i[:2] == 'UR' and len(i) == 3:
        print('URI', end = '')
    else:
        print(i, end = '')
    j += 1
print()