from random import randint

def sort(lista):
    print('Sorteando 5 valores da lista:')
    for cont in range(0,5):
        n = randint(1,10)
        lista.append(n)
        print(f'{n}',end=' ')
    print('Fim')
    
def somap(lista):
    soma = 0
    for i in lista:
        if i % 2 == 0:
            soma += i
    print(f'Somando os valores pares de {lista}, temos {soma}')

    
numeros = list()
sort(numeros)
somap(numeros)




