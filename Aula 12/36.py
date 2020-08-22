vcasa = float(input('Digite o Valor da Casa:\n'))
qanos = float(input('Digite quantos anos deseja pagar:\n'))
sal = float(input('Digite o seu salário:\n'))

prest = vcasa / (qanos*12)
minim = sal * 30 / 100

if prest <= minim:
    print('Empréstimo pode ser APROVADO!')

else:
    print('Empréstimo NEGADO!')
