print('Gerador de PA')
print('-=-'*10,'\n')
pri = int(input('Digite o primeiro termo:'))
r = int(input('Digite a razão:'))

mais = 10
cont = total = 0

while mais != 0:
    total = total + mais
    while cont <= total:
        print(f'{pri}',end=' > ')
        pri += r
        cont += 1
    print('Pausa')
    mais = int(input('Deseja mais quantos elementos?'))

print(f'Ao total foram mostrados {total} elementos de uma PA')        
