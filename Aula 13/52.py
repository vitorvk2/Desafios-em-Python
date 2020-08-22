num1 = int(input('Digite um número:'))
cont = 0

for c in range (1, num1+1):
    if num1 % c == 0:
        print('\33[32m',end=' ')
        cont += 1
    else:
        print('\033[31m',end=' ')
    print(f'{(c)}',end=' ')
print(f'\n\n\033[mO número {(num1)} foi divisível {(cont)} vezes')

if cont == 2:
    print(f'Por este motivo, o {(num1)} é PRIMO')

else:
    print(f'Por este motivo, o {(num1)} NÃO É PRIMO')