Votes = []
count = 0
while True:
  try:
    N = int(input(''))
    Votes = list(map(int, input().split()))
    for i in Votes:
        if i == 1:
            count += 1
    if count >= (2 * len(Votes)) / 3:
        print('impeachment')
        count = 0
    else:
        print('acusacao arquivada')
        count = 0
  except EOFError:
    break