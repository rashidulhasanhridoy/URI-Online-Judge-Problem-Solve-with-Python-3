Numbes = []
while True:
  try:
   A, B = map(int, input().split())
   C = A ^ B
   print(C)
  except EOFError:
    break