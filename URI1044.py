linea = str(input())
splita = linea.split()
A = int(splita[0])
B = int(splita[1])
if A % B == 0 or B % A == 0:
    print('Sao Multiplos')
else:
    print('Nao sao Multiplos')