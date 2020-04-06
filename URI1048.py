salary = float(input(''))
if salary >= 0 and salary <= 400:
    earned = salary * 0.15
    salary = salary + earned
    print('Novo salario: %0.2f' %salary)
    print('Reajuste ganho: %0.2f' %earned)
    print('Em percentual: 15 %')
elif salary > 400 and salary <= 800:
    earned = salary * 0.12
    salary = salary + earned
    print('Novo salario: %0.2f' %salary)
    print('Reajuste ganho: %0.2f' %earned)
    print('Em percentual: 12 %')
elif salary > 800 and salary <= 1200:
    earned = salary * 0.10
    salary = salary + earned
    print('Novo salario: %0.2f' %salary)
    print('Reajuste ganho: %0.2f' %earned)
    print('Em percentual: 10 %')
elif salary > 1200 and salary <= 2000:
    earned = salary * 0.07
    salary = salary + earned
    print('Novo salario: %0.2f' %salary)
    print('Reajuste ganho: %0.2f' %earned)
    print('Em percentual: 7 %')
elif salary > 2000.00:
    earned = salary * 0.04
    salary = salary + earned
    print('Novo salario: %0.2f' %salary)
    print('Reajuste ganho: %0.2f' %earned)
    print('Em percentual: 4 %')