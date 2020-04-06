while True:
  try:
     X1, Y1, X2, Y2, V, R1, R2 = map(int, input().split())
     X = (X2 - X1) ** 2
     Y = (Y2 - Y1) ** 2
     D = (X + Y) ** 0.5
     D = D + (V * 1.50)
     T = R1 + R2
     if D <= T:
         print('Y')
     else:
         print('N')
  except EOFError:
      break