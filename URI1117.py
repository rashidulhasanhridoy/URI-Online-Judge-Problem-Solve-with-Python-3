count = 0
sum = 0
while True:
    X = float(input(''))
    if X >= 0 and X <= 10:
        count += 1
        sum += X
        if count == 2:
            average = sum / count
            print('media = %0.2f' %average)
            break
    else:
        print('nota invalida')
