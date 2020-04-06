N = int(input(''))
for i in range(N):
    P1 = str(input(''))
    P2 = str(input(''))
    if P1[1] == 't' and P2[1] == 'e':
        print('Jogador 1 venceu')
    elif P1[1] == 'e' and P2[1] == 't':
        print('Jogador 2 venceu')
    elif P1[1] == 'e' and P2[1] == 'a':
        print('Jogador 1 venceu')
    elif P1[1] == 'a' and P2[1] == 'e':
        print('Jogador 2 venceu')
    elif P1[1] == 't' and P2[1] == 'a':
        print('Jogador 1 venceu')
    elif P1[1] == 'a' and P2[1] == 't':
        print('Jogador 2 venceu')
    elif P1[1] == 'a' and P2[1] == 'a':
        print('Ambos venceram')
    elif P1[1] == 'e' and P2[1] == 'e':
        print('Sem ganhador')
    elif P1[1] == 't' and P2[1] == 't':
        print('Aniquilacao mutua')