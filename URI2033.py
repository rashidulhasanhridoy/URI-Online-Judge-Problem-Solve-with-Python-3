import math
while True:
  try:
    C = float(input(''))
    I = float(input(''))
    N = int(input(''))
    SIMPLE = C * I * N
    COMPOSTO = (C * pow((1 + I),  N)) - C
    DIFERENCA = math.fabs(SIMPLE - COMPOSTO)
    print('DIFERENCA DE VALOR = %0.2f' %DIFERENCA)
    print('JUROS SIMPLES = %0.2f' %SIMPLE)
    print('JUROS COMPOSTO = %0.2f' %COMPOSTO)
  except EOFError:
      break
      #not accepected