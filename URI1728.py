def reverse(s):
  str = ""
  for i in s:
    str = i + str
  return str
while True:
    X = str(input(''))
    if X == '0+0=0':
        print('True')
        break
    for p1, item in enumerate(X):
        if item == '+':
            Y = p1
    for p2, item in enumerate(X):
        if item == '=':
            Z = p2
    A = int(reverse(X[:Y]))
    B = int(reverse(X[Y+1:Z]))
    C = int(reverse(X[Z+1:]))
    if A + B == C:
        print('True')
    else:
        print('False')