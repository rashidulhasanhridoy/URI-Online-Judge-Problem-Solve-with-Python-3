count = 0
N, I = map(int, input().split())
while True:
  try:
      X, Y = map(int, input().split())
      if X == I and Y == 0:
         count += 1
  except EOFError:
    break
print(count)