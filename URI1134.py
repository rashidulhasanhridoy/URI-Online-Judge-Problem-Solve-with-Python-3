Alcohol = 0
Gasoline = 0
Diesel = 0
while True:
    X = int(input(''))
    if X >= 1 and X <= 4:
        if X == 1:
            Alcohol += 1
        elif X == 2:
            Gasoline += 1
        elif X == 3:
            Diesel += 1
        elif X == 4:
            break
print('MUITO OBRIGADO')
print('Alcool:', Alcohol)
print('Gasolina:', Gasoline)
print('Diesel:', Diesel)