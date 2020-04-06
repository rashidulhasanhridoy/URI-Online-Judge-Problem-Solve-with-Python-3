N = int(input(''))
Coelho = 0
Rato = 0
Sapo = 0
for i in range(N):
    linea = str(input(''))
    splita = linea.split()
    nunber = int(splita[0])
    name = str(splita[1])
    if name == 'C':
        Coelho += nunber
    elif name == 'R':
        Rato += nunber
    elif name == 'S':
        Sapo += nunber
total = Coelho + Rato + Sapo
print('Total:',total,'cobaias')
print('Total de coelhos:', Coelho)
print('Total de ratos:', Rato)
print('Total de sapos:', Sapo)
pCoelho = (Coelho / total) * 100
pRato = (Rato / total) * 100
pSapo = (Sapo / total) * 100
print('Percentual de coelhos: %0.2f' %pCoelho, '%')
print('Percentual de ratos: %0.2f' %pRato, '%')
print('Percentual de sapos: %0.2f' %pSapo, '%')