salary = float(input(''))
if salary <= 2000:
    print('Isento')
elif salary >= 2000 and salary <= 3000:
    tax = (salary - 2000) * 0.08
    print('R$ %0.2f' %tax)
elif salary >= 3000 and salary <= 4500:
    tax1 = 1000 * 0.08
    tax2 = ((salary - 3000) * 0.18)
    tax = tax1 + tax2
    print('R$ %0.2f' %tax)
elif salary > 4500:
    tax1 = 1000 * 0.08
    tax2 = 1500 * 0.18
    tax3 = (salary - 4500) * 0.28
    tax = tax1 + tax2 + tax3
    print('R$ %0.2f' % tax)