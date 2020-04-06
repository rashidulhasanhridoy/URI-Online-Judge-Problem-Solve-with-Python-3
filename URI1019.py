N = int(input(''))
hours = N // 3600
minutes = (N - (hours * 3600)) // 60
seconds = (N - ((hours * 3600) + (minutes * 60)))
print(hours, ':', minutes, ':', seconds, sep = '')