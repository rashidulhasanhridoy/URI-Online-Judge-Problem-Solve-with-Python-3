while True:
    S = input().strip()
    if S == '0':
        break
    else:
        y = len(S)
        sum = 1
        for i in range(1,y):
            sum = sum * (y - i)
        print('%d' %(y * sum))