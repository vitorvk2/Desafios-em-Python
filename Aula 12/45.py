from random import randint
from time import sleep

start = 's'

while start == 's':
    jo = int(input('''
Suas opções:
[ 1 ] PEDRA
[ 2 ] PAPEL
[ 3 ] TESOURA
Qual é a sua jogada?'''))

    com = randint(1,3)
    if com == 1:
        comj = 'PEDRA'
    elif com == 2:
        comj = 'PEPEL'
    else:
        comj = 'TESOURA'

    if jo == 1:
        j = 'PEDRA'
    elif jo == 2:
        j = 'PEPEL'
    elif jo == 3:
        j = 'TESOURA'
    else:
        j = 'Caractere inválido'


    sleep(1)
    print('\nJO')
    sleep(1)
    print('KEN')
    sleep(1)
    print('PO!!\n')
    print('-=-'*15)
    print(f'Computador jogou {(comj)}\nJogador jogou {(j)}')
    print('-=-'*15)

    if com == 1:
        if jo == 1:
            print('EMPATE')
        elif jo == 2:
            print('JOGADOR VENCE')
        elif jo == 3:
            print('COMPUTADOR VENCE')
        else:
            print('JOGADA INVÁLIDA')

    if com == 2:
        if jo == 1:
            print('COMPUTADOR VENCE')
        elif jo == 2:
            print('EMPATE')
        elif jo == 3:
            print('JOGADOR VENCE')
        else:
            print('JOGADA INVÁLIDA')

    if com == 3:
        if jo == 1:
            print('JOGADOR VENCE')
        elif jo == 2:
            print('COMPUTADOR VENCE')
        elif jo == 3:
            print('EMPATE')
        else:
            print('JOGADA INVÁLIDA')

    start = str(input('\nDeseja jogar novamente? (s ou n):'))
    start = str.lower(start)
print('Fim do Game!')