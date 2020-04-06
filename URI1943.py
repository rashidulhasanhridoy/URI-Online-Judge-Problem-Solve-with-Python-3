K = int(input(''))
if K == 1:
    print('Top 1')
elif K >= 2 and K <= 3:
    print('Top 3')
elif K >= 4 and K <= 5:
    print('Top 5')
elif K >= 6 and K <= 10:
    print('Top 10')
elif K >= 11 and K <= 25:
    print('Top 25')
elif K >= 26 and K <= 50:
    print('Top 50')
elif K >= 51 and K <= 100:
    print('Top 100')
