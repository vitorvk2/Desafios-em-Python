import funcoes 

def leiaInt(msg):
    while True:
        try:
            n = int(input(msg))
        except(ValueError, TypeError):
            print('ERRO: por favor, digite um número inteiro válido')
            continue
        except KeyboardInterrupt:
            print('O usuário interrompeu a entrada de dados')
            return 0
        else:
            return n

def leiaFloat(msg):
    while True:
        try:
            n2 = float(input(msg))
        except(ValueError, TypeError):
            print('ERRO: por favor, digite um número real.')
            continue
        else:
            return n2


num1 = leiaInt('Digite um valor:')
print(f'O valor digitado foi {num1}')
num2 = leiaFloat('Digite um valor:')
print(f'O valor digitado foi {num2}')