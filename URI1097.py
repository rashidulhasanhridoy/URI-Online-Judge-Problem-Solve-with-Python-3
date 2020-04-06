I = -1
a, b, c = 7, 6, 5
for i in range(1, 6):
    i = I + 2
    print('I=%d J=%d' % (i, a))
    a = a + 2
    print('I=%d J=%d' % (i, b))
    b = b + 2
    print('I=%d J=%d' % (i, c))
    c = c + 2
    I = i