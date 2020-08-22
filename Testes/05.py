nome = input('Qual é o Nome do Aluno?')
print ('')
print('Referente as notas:')
n1 = int(input('Qual é a primeira nota do aluno?'))
n2 = int(input('Qual é a Segunda nota do Aluno?'))

m = int((n1+n2)/2)

print('O aluno {}, obteve a nota final: {}'.format(nome,m))