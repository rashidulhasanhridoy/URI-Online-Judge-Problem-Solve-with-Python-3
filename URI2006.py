sum = 0
T = int(input(''))
A, B, C, D, E = map(int, input().split())
Numbers = [A, B, C, D, E]
for i in Numbers:
    if i == T:
        sum += 1
print(sum)