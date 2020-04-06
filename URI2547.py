count = 0
while True:
  try:
    N, Min, Max = map(int, input().split())
    for i in range(N):
        X = int(input(''))
        if X >= Min and X <= Max:
            count += 1
    print(count)
    count = 0
  except EOFError:
    break