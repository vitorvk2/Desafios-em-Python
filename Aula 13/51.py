print ('='*24)
print ('    TERMOS DE UMA PA  ')
print ('='*24)
soma = 0

n1= int(input('Primeiro termo:'))
n2 = int(input('Numero de termos:'))
r = int(input('Razão:'))

dec = n1+(n2-1)*r
for c in range(n1, dec + r, r):
    soma += c
    print(f'{(c)}',end=' > ')

print('ACABOU\n')
print(f'A soma de todos os termos é: {(soma)}')
