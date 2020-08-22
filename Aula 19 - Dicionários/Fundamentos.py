#Dicionário normal
pessoas = {'Nome': 'Vitor', 'Sexo': 'M', 'Idade' : '18'}
pessoas['Peso'] = '50'
del pessoas['Sexo']
for k, v in pessoas.items():
    print(f'{k} = {v}')

print()

#Dicionário dentro de Lista
brasil = []
estado1 = {'uf': 'São Paulo', 'Sigla': 'SP'}
estado2 = {'uf': 'Rio de Janeiro', 'Sigla' : 'RJ'}

brasil.append(estado1)
brasil.append(estado2)

print(brasil[0]['uf'])

print()

#Input no Dicionário
estado = dict()
brasil = list()

for c in range(3):
    estado['uf'] = str(input('Unidade Federativa:'))
    estado['sigla'] = str(input('Sigla do Estado:'))
    brasil.append(estado.copy())

for e in brasil:
    #for k, v in e.items():
    #    print(f'O campo {k} tem o valor {v}.')
    for v in e.values():
        print(v, end=' ')
    print()