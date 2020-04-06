X1, X2, X3, X4, X5 = map(int, input().split())
Y1, Y2, Y3, Y4, Y5 = map(int, input().split())
if ((X1 == 0 and Y1 == 1) or (X1 == 1 and Y1 == 0)) and ((X2 == 0 and Y2 == 1) or (X2 == 1 and Y2 == 0)) and ((X3 == 0 and Y3 == 1) or (X3 == 1 and Y3 == 0)) and ((X4 == 0 and Y4 == 1) or (X4 == 1 and Y4 == 0)) and ((X5 == 0 and Y5 == 1) or (X5 == 1 and Y5 == 0)):
    print('Y')
else:
    print('N')