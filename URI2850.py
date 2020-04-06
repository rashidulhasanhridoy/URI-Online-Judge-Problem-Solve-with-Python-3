while True:
  try:
     X = str(input(''))
     if X[0] == 'e':
         print('ingles')
     elif X[0] == 'd':
         print('frances')
     elif X[0] == 'n':
         print('portugues')
     elif X[0] == 'a':
         print('caiu')
  except EOFError:
      break