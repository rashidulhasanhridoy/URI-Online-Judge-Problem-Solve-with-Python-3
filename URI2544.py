while True:
  try:
    N = int(input(''))
    if N == 1:
        print('0')
    else:
        count = 0
        sum = 1
        while True:
            sum = sum * 2
            count += 1
            if sum > N:
                break
            if sum == N:
                break
        print(count)
  except EOFError:
    break