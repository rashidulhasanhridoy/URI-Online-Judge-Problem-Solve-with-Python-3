linea = str(input(''))
lineb = str(input(''))
splita = linea.split()
splitb = lineb.split()
code1 = int(splita[0])
unit1 = int(splita[1])
price1 = float(splita[2])
code2 = int(splitb[0])
unit2 = int(splitb[1])
price2 = float(splitb[2])
total = (unit1 * price1) + (unit2 * price2)
print('VALOR A PAGAR: R$ %0.2f' %total)