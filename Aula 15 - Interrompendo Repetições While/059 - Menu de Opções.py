from time import sleep
op = 4

while op != 5:
    if op == 4:
        n1 = int(input('\nDigite o primeiro número:'))
        n2 = int(input('Digite o segundo número:'))

    while True:
        op = int(input('''
[ 1 ] somar
[ 2 ] multiplicar
[ 3 ] maior
[ 4 ] inserir novos números
[ 5 ] sair do programa
>>>>> Digite sua opção:'''))
        sleep(1)
        if op == 1:
            print(f'A soma entre {n1} e {n2} é {n1+n2}.')
            break
        elif op == 2:
            print(f'A multiplicação de {n1} e {n2} é {n1*n2}.')
            break
        elif op == 3:
            if n1 > n2:
                print(f'{n1} é MAIOR que {n2}.')
                break
            elif n1 < n2:
                print(f'{n1} é MENOR que {n2}.')
                break
            else:
                print(f'Números Iguais.')
                break
        elif op == 4 or op == 5:
            break
        else:
            print('Número Inválido! Tente novamente')
print('\nFim do Programa!!')