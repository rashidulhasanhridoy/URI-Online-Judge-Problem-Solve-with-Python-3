sum = 0
while True:
    T = int(input(''))
    if T == 0:
        break
    else:
        for i in range(T):
            X = str(input(''))
            Z = X.split()
            Y = int(Z[0])
            B = str(Z[1])
            if B == 'suco':
                sum += (Y * 120)
            elif B == 'morango':
                sum += (Y * 85)
            elif B == 'mamao':
                sum += (Y * 85)
            elif B == 'goiaba':
                sum += (Y * 70)
            elif B == 'manga':
                sum += (Y * 56)
            elif B == 'laranja':
                sum += (Y * 50)
            elif B == 'brocolis':
                sum += (Y * 34)
        if sum >= 110 and sum <= 130:
                print(sum, 'mg')
                sum = 0
        elif sum < 110:
            C = 110 - sum
            print('Mais', C, 'mg')
            sum = 0
        elif sum > 130:
            C = sum - 130
            print('Menos', C, 'mg')
            sum = 0