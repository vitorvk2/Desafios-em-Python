numero = int(input('Digite a quantidade de elementos da serie de Fibonacci:'))
fibo = 1
ant = 0
for i in range(numero):
    print(fibo, end = ' > ')
    ant, fibo = fibo, fibo + ant

print('Fim')
