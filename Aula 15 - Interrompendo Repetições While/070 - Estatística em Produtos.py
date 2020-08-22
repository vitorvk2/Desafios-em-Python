soma = mais1000 = menor = cont =0
barato = ' '

while True:
    prod = str(input('\nNome do Produto:'))
    preç = int(input('Preço do produto R$:'))
    cont += 1
    soma += preç
    
    if preç >= 1000:
        mais1000 += 1
    if cont == 1 or preç < menor:
        menor = preç
        barato = prod
        
    resp = ' '
    while resp not in 'SN':
        resp = str(input('Deseja Continuar?')).strip().upper()[0]
    if resp == 'N':
        break

print('{:-^40}'.format('FIM DO PROGRAMA'))
print(f'O total de todos os produtos é R${soma}')
print(f'A quantidade de produtos acima de R$ 1000,00 é :{mais1000}')
print(f'O produto mais barato foi {barato} e custa R${menor}')