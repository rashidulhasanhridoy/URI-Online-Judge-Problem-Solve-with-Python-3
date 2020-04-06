days = [31, 29, 31, 30, 31, 30, 31, 31, 30, 31, 30, 25]
while True:
  try:
    M, D = map(int, input().split())
    if M == 12 and D == 25:
        print('E natal!')
    elif M == 12 and D == 24:
        print('E vespera de natal!')
    elif M == 12 and D > 25:
        print('Ja passou!')
    else:
        N = days[M -1] - D
        for i in range(M, 12, 1):
            N += days[i]
        print('Faltam %d dias para o natal!' %N)
  except EOFError:
    break