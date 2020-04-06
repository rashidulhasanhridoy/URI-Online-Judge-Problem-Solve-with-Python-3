N = int(input(''))
count = 0
for i in range(N, N + 12):
    if i % 2 != 0:
        print(i, end = '\n')
        count += 1
        if count == 6:
            break