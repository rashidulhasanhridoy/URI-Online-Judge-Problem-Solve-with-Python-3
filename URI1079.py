N = int(input(''))
Numbers = []
for i in range(N):
   A, B, C = map(float, input().split())
   average = ((A * 2) + (B * 3) + (C * 5)) / (2 + 3 + 5)
   print('%0.1f' %average)
