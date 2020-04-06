large = 0
Numbers = []
for i in range(100):
    X = int(input(''))
    Numbers.insert(i, X)
for i in Numbers:
    if i > large:
        large = i
print(large)
position = Numbers.index(large) + 1
print(position)
