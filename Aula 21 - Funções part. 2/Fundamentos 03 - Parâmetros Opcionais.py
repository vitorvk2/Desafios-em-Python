#Em uma fução criada por você, alguma das entrada de dados podem
#ser opcionais

#Exemplo:
def cont(a, b ,c=1):
    for i in range(a,b+1,c):
        print(f'{i}',end=' > ')
    print('Fim')

cont(1,742,7)

#O 'c=' diz que caso o usuário não insira o c, ele irá possuir o valor 1