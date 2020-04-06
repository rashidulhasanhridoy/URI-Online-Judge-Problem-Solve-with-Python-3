N = int(input(''))
print(N)
nota100 = N // 100
print(nota100, 'nota(s) de R$ 100,00')
nota50 = (N - (nota100 * 100)) // 50
print(nota50, 'nota(s) de R$ 50,00')
nota20 = (N - ((nota100 * 100) + (nota50 * 50))) // 20
print(nota20, 'nota(s) de R$ 20,00')
nota10 = (N - ((nota100 * 100) + (nota50 * 50) + (nota20 * 20))) // 10
print(nota10, 'nota(s) de R$ 10,00')
nota5 = (N - ((nota100 * 100) + (nota50 * 50) + (nota20 * 20) + (nota10 * 10))) // 5
print(nota5, 'nota(s) de R$ 5,00')
nota2 = (N - ((nota100 * 100) + (nota50 * 50) + (nota20 * 20) + (nota10 * 10) + (nota5 * 5))) // 2
print(nota2, 'nota(s) de R$ 2,00')
nota1 = (N - ((nota100 * 100) + (nota50 * 50) + (nota20 * 20) + (nota10 * 10) + (nota5 * 5) + (nota2 * 2))) // 1
print(nota1, 'nota(s) de R$ 1,00')