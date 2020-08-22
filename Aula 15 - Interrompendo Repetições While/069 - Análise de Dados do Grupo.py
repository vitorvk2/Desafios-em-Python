print('-'*20)
print('Cadastre uma Pessoa!')
print('-'*20,'\n')

maior = cont = mulher = homem = 0

while True:
    sexo = str(input('\nSexo: [M/F]')).strip().upper()[0]
    while sexo not in 'MF':
        sexo = str(input('Caractere Inválido, tente novamente:')).strip().upper()[0]
    idade = int(input('Idade:'))
    while idade <= 0:
        idade = int(input('Idade inválida, tente novamente:'))
    cont += 1
    if idade > 18:
        maior += 1
    if sexo == 'M':
        homem += 1
    if sexo == 'F':
        if idade <= 20:
            mulher += 1
    op = str(input('Deseja continuar? [S/N]')).strip().upper()[0]
    while op not in 'SN':
        op = str(input('Caractere Inválido, digite novamente!')).strip().upper()[0]
    if op == 'N':
        break
    else:
        continue

print(f'\nNúmero de pessoas cadastradas: {cont}')
print(f'Total de pessoas com mais de 18 anos: {maior}.')
print(f'Ao todo temos {homem} homens cadastrados.')
print(f'E temos {mulher} mulheres com menos de 20 anos.\nFim do Programa')


    

