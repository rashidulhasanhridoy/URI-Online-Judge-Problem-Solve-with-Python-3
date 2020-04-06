i, j = 1, 60
for i in range(1, j, 3):
    print('I=', i, ' J=', j, sep='')
    if j == 0:
        break
    j = j - 5