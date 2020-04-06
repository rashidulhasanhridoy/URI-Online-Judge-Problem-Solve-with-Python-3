C = int(input(''))
for i in range(C):
    M, N = map(str, input('').split())
    X = M.lower()
    Y = N.lower()
    if X == Y:
        print('empate')
    elif X == 'tesoura' and Y == 'papel':
        print('rajesh')
    elif X == 'papel' and Y == 'tesoura':
        print('sheldon')
    elif X == 'papel' and Y == 'pedra':
        print('rajesh')
    elif X == 'pedra' and Y == 'papel':
        print('sheldon')
    elif X == 'pedra' and Y == 'lagarto':
        print('')
    elif X == 'lagarto' and Y == 'pedra':
        print('sheldon')
    elif X == 'lagarto' and Y == 'spock':
        print('rajesh')
    elif X == 'spock' and Y == 'lagarto':
        print('sheldon')
    elif X == 'spock' and Y == 'tesoura':
        print('rajesh')
    elif X == 'tesoura' and Y == 'spock':
        print('sheldon')
    elif X == 'tesoura' and Y == 'lagarto':
        print('rajesh')
    elif X == 'lagarto' and Y == 'tesoura':
        print('sheldon')
    elif X == 'lagarto' and Y == 'papel':
        print('rajesh')
    elif X == 'papel' and Y == 'lagarto':
        print('sheldon')
    elif X == 'papel' and Y == 'spock':
        print('rajesh')
    elif X == 'spock' and Y == 'papel':
        print('sheldon')
    elif X == 'spock' and Y == 'pedra':
        print('rajesh')
    elif X == 'pedra' and Y == 'spock':
        print('sheldon')
    elif X == 'pedra' and Y == 'tesoura':
        print('rajesh')
    elif X == 'tesoura' and Y == 'pedra':
        print('sheldon')