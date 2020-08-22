import time

num = int(input('Digite um número inteiro:'))
opc = int(input('''
Bases de conversão:
1 - para Binário;
2 - para Octal;
3 - para Hexadecimal.

Escolha uma delas:'''))

print('\nProcessando\n')
time.sleep(0.3)

if opc == 1:
    print(f'{(num)} convertido para Binário é {(bin(num)[2:])}')
elif opc == 2:
    print(f'{(num)} convertido para Octal é {(oct(num)[2:])}')
elif opc == 3:
    print(f'{(num)} convertido para Hexadecimal é {(hex(num)[2:])}')
else:
    print('Opção inválida')

print('\nObrigado!')