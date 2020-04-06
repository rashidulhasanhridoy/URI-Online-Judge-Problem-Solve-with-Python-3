while True:
  try:
   Numbers = []
   N = int(input(''))
   for i in range(N):
       X = float(input(''))
       Numbers.insert(i, X)
   Y = min(Numbers)
   print(Y)
   Numbers.clear()
  except EOFError:
    break