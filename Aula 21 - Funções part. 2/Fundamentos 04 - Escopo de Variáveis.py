#exemplo 1
def teste():
    x = 8
    print(f'Na função teste, n vale {n}')
    print(f'Na função teste, x vale {x}')

#Programa Principal
n = 2
print(f'No programa principal, n vale {n}')
teste()

#As variáveis podem ser utilizadas de duas formas, globalmente e localmente.

#no exemplo acima, o 'n=2' é uma variável global, podendo ser utilizada dentro
#e fora de uma função.

#Já o 'x=8' é uma variável local, podendo ser utilizada apenas e exclusivamente
#dentro da função que ela foi declarada. 

print()

#Exemplo 2
def funcao():
    n1 = 4
    print(f'N1 dentro vale {n1}')

n1 = 2
funcao()
print(f'N1 fora vale {n1}')

#Se uma varável receber dois valores dentro da função e fora dela, a mesma terá
#valores diferentes, sendo o 'n1=4' exclusivo da função e 'n1 = 2' globalmente.

print()

#Exemplo 3
def funcao():
    global n1
    n1 = 4
    print(f'N1 dentro vale {n1}')

n1 = 2
funcao()
print(f'N1 fora vale {n1}')

#Se for definido o 'global n1' dentro da função, o exemplo2 será anulado.
#sendo assim, o valor 'n1 = 4' será o global.
