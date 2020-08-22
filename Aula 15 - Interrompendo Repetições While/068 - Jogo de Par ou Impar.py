from random import randint

contador_jogo = cont_gan = cont_per = 0

while contador_jogo < 3:
    print('\n\n')
    print('-=-'*15)
    print('VAMOS JOGAR PAR OU ÍMPAR')
    print('-=-'*15,'\n')
    jog_usu = int(input('Diga um Valor:'))
    PouI = str(input('Par ou Ímpar? [P/I] ou [stop]:')).upper()
    while PouI not in 'PISTOP':
        PouI = str(input('Caractere inválido, digite novamente:')).upper()

    while True:
        jog_mac = randint(1,10)
        if jog_mac % 2 == 1:
            jog_macI = jog_mac
            break
        else:
            continue

    while True:
        jog_mac = randint(1,10)
        if jog_mac % 2 == 0:
            jog_macP = jog_mac
            break
        else:
            continue

    if PouI == 'P':
        soma = jog_usu + jog_macP
        print('-=-'*15)
        print(f'Você jogou {(jog_usu)} e a máquina {(jog_macP)}. O total é {(soma)}')
        print('-=-'*15,'\n')
        if soma % 2 == 0:
            print(f'DEU PAR!\nVocê venceu!')
            cont_gan += 1
        else:
            print('DEU ÍMPAR!\nVocê perdeu, tente novamente!')
            cont_per += 1

    elif PouI == 'I':
        soma = jog_usu + jog_macI
        print('-=-'*15)
        print(f'Você jogou {(jog_usu)} e a máquina {(jog_macI)}. O total é {(soma)}')
        print('-=-'*15,'\n')
        if soma % 2 == 1:
            print(f'DEU ÍMPAR!\nVocê venceu!')
            cont_gan += 1
        else:
            print('DEU PAR!\nVocê perdeu, tente novamente!')
            cont_per += 1

    elif PouI == 'STOP':
        break


    contador_jogo += 1

print(f'\nVocê ganhou {(cont_gan)} vezes e perdeu {(cont_per)} vezes.')
print('FIM DO PROGRAMA, obrigado por jogar!')
