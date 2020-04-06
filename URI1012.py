linea = str(input(''))
splita = linea.split()
A = float(splita[0])
B = float(splita[1])
C = float(splita[2])
TRIANGULO = 0.5 * A * C
print('TRIANGULO: %0.3f' %TRIANGULO)
CIRCULO = 3.14159 * (C ** 2)
print('CIRCULO: %0.3f' %CIRCULO)
TRAPEZIO = ((A + B)/ 2) * C
print('TRAPEZIO: %0.3f' %TRAPEZIO)
QUADRADO = B * B
print('QUADRADO: %0.3f' %QUADRADO)
RETANGULO = A * B
print('RETANGULO: %0.3f' %RETANGULO)