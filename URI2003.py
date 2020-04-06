while True:
  try:
      H, M = map(int, input().split(':'))
      if H < 7:
          print('Atraso maximo: 0')
      elif H == 7 and M == 0:
          print('Atraso maximo: 0')
      else:
          RM = ((H + 1) - 8) * 60 + M
          print('Atraso maximo:', RM)
  except EOFError:
    break