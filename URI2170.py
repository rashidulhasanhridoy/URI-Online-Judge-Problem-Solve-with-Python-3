i = 1
while True:
  try:
      X, Y = map(float, input('').split())
      M = Y - X
      Z = (M * 100) / X * 1.00
      print('Projeto %d:' %i)
      i += 1
      print('Percentual dos juros da aplicacao: %0.2f' %Z, '%')
      print('', end = '\n')
  except EOFError:
      break