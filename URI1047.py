sh, sm, fh, fm = map(int, input('').split())
if sh == sm and sm == fh and fh == fm and fm == sh:
    print('O JOGO DUROU 24 HORA(S) E 0 MINUTO(S)')
elif sh <= fh:
    if sm < fm:
        hours = fh - sh
        minutes = fm - sm
        print('O JOGO DUROU', hours, 'HORA(S) E', minutes, 'MINUTO(S)')
    else:
        hours = (fh - sh) - 1
        minutes = (60 - sm) + fm
        print('O JOGO DUROU', hours, 'HORA(S) E', minutes, 'MINUTO(S)')
elif sh >= fh:
    if sm > fm:
        hours = (24 - sh) + fh - 1
        minutes = (60 - sm) + fm
        print('O JOGO DUROU', hours, 'HORA(S) E', minutes, 'MINUTO(S)')
    else:
        hours = ((24 - sh) + fh) + (((60 - sm) + fm) // 60) - 1
        minutes = (((60 - sm) + fm) % 60)
        print('O JOGO DUROU', hours, 'HORA(S) E', minutes, 'MINUTO(S)')