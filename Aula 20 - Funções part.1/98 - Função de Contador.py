def prin(frase):
    x = len(frase) + 4
    print('~'*x)
    print(f'  {frase}')
    print('~'*x)

def cont(a,b,c):
    for i in range(a,b+1,c):
        print(f'{i}',end=' > ')
    print('Fim')


#Programa Principal
prin('Contagem de 1 até 10, de 1 em 1')
cont(1,10,1)
print()

z = 20

prin(f'Contagem de 10 até 0, de 2 em 2 {z}')
cont(10,0,-2)
print()

prin('Insira dos Dados')
a = int(input('Início:'))
b = int(input('Fim:'))
c = int(input('Passo:'))
cont(a,b,c)