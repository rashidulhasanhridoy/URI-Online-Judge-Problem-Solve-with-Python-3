while True:
  try:
   S, Va, Vb = map(int, input().split())
   if Va < Vb:
       print('impossivel')
   else:
       t = S/ ((Va - Vb) * 1.0)
       print('%0.2f' %t)
  except EOFError:
    break