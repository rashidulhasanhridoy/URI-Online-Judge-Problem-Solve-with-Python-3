linea = str(input())
splita = linea.split()
A = float(splita[0])
B = float(splita[1])
C = float(splita[2])
D = float(splita[3])
Media = ((A * 2) + (B * 3) + (C * 4) + (D * 1)) / (2 + 3 + 4 +1)
print('Media: %0.1f' %Media)
if Media >= 7.0:
    print('Aluno aprovado.')
elif Media < 5.0:
    print('Aluno reprovado.')
elif Media >= 5.0 and Media <= 6.9:
    print('Aluno em exame.')
    E = float(input(''))
    Average = (Media + E) / 2
    if Average >= 5.0:
        print('Nota do exame: %0.1f' %E)
        print('Aluno aprovado.')
        print('Media final: %0.1f' %Average)
    elif Average <= 4.9:
        print('Nota do exame: %0.1f' % E)
        print('Aluno reprovado.')
        print('Media final: %0.1f' % Average)