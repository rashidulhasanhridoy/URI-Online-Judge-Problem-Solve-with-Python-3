T = int(input(''))
str1 = ' - A porta abriu!'
str2 = ' - A porta fechou!'
for i in range(T):
    h, m, o = map(int, input().split())
    H = str(h)
    M = str(m)
    if len(H) == 1 and len(M) == 2:
        if o == 1:
            print('0', h, ':', m, str1, sep = '')
        elif o == 0:
            print('0', h, ':', m, str2, sep='')
    elif len(H) == 2 and len(M) == 1:
        if o == 1:
            print(h, ':', '0', m, str1, sep = '')
        elif o == 0:
            print(h, ':', '0', m, str2, sep='')
    elif len(H) == 1 and len(M) == 1:
        if o == 1:
            print('0', h, ':', '0', m, str1, sep = '')
        elif o == 0:
            print('0', h, ':', '0', m, str2, sep='')
    elif len(H) == 2 and len(M) == 2:
        if o == 1:
            print(h, ':', m, str1, sep = '')
        elif o == 0:
            print(h, ':', m, str2, sep='')
