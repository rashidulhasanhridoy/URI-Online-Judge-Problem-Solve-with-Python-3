N = int(input(''))
year = N // 365
month = (N - (year * 365)) // 30
days = (N - (year * 365) - (month * 30))
print(year, 'ano(s)')
print(month, 'mes(es)')
print(days, 'dia(s)')