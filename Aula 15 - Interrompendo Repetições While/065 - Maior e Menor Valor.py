soma = cont = maior = menor = 0
op = 's'
while op in 'sS':
    num = int(input('Digite um número:'))
    cont += 1
    soma += num
    if cont == 1:
        maior = menor = num
    else:
        if num > maior:
            maior = num
        if num < menor:
            menor = num
    op = str(input('Deseja Continuar? [S/N]')).strip().upper()[0]
media = soma / cont

print(f'A média é {media}.\nO maior número é {maior} e o menor {menor}')
