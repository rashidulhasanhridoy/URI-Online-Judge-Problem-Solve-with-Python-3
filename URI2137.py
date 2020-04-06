while True:
  Z = []
  try:
     N = int(input(''))
     for i in range(N):
         X = int(input(''))
         Z.append(X)
     Y = sorted(Z)
     for i in Y:
         print("{0:04d}".format(i))
         Z = []
  except EOFError:
      break