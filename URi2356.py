while True:
  try:
      D = str(input(''))
      S = str(input(''))
      if S in D:
          print('Resistente')
      else:
          print('Nao resistente')
  except EOFError:
      break