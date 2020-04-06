start, end = map(int, input().split())
if start == end:
    print('O JOGO DUROU 24 HORA(S)')
elif start > end:
    time = (24 - start) + end
    if time >= 24:
        day = time // 24
        hours = time % 24
        print(day, 'JOGO DUROU', hours, 'HORA(S)')
    else:
        print('O JOGO DUROU', time, 'HORA(S)')
elif start < end:
    time = end - start
    if time >= 24:
        day = time // 24
        hours = time % 24
        print(day, 'JOGO DUROU', hours, 'HORA(S)')
    else:
        print('O JOGO DUROU', time, 'HORA(S)')