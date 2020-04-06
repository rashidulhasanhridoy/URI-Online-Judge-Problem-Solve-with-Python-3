N = int(input(''))
count = 0
I = -1
for i in range(N):
    i = I + 2
    print(i, i + 1, i + 2, 'PUM')
    i = i + 2
    count += 1
    I = i
    if count == N:
        break