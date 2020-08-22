aluno = {}

aluno['Nome'] = str(input('Nome do Aluno:'))
aluno['Nota'] = float(input('Média do Aluno:'))

if aluno['Nota'] >= 5:
    aluno['Situação'] = 'Aprovado'
else:
    aluno['Situação'] = 'Reprovado'

print('-'*20)
print(f'''- Nome == {aluno['Nome']}
- Média == {aluno["Nota"]}
- Situação == {aluno["Situação"]}''')
