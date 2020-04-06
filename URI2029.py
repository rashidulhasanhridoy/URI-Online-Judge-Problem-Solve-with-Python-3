Numbers = []
while True:
  try:
     V = float(input(''))
     D = float(input(''))
     R = D / 2
     A = 3.14 * (R ** 2)
     H = V / A
     print('ALTURA = %0.2f' %H)
     print('AREA = %0.2f' %A)
  except EOFError:
    break