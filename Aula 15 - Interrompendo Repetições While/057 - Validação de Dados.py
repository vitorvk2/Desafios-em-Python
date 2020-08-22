sexo = str(input('Informe seu Sexo: [M/F]')).strip().upper()[0]
while sexo not in 'MF':
    sexo =str(input('Dados inválidos, informe seu sexo:')).strip().upper()[0]
print(f'Sexo {sexo} registrado com sucesso.')
