linea = str(input(''))
splita = linea.split()
X = int(splita[0])
Y = int(splita[1])
if X == 1:
    total = Y * 4.00
elif X == 2:
    total = Y * 4.50
elif X == 3:
    total = Y * 5.00
elif X == 4:
    total = Y * 2.00
elif X == 5:
    total = Y * 1.50
print('Total: R$ %0.2f' %total)