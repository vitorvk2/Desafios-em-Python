from datetime import datetime

dados = {}
dados['nome'] = str(input('Nome:'))
nasc = int(input('Data de Nascimento:'))
dados['idade'] = datetime.now().year - nasc
dados['ctps'] = int(input('Carteirda de Trabalho ([0] não possui):'))
if dados['ctps'] != 0:
    dados['contratação'] = int(input('Ano de Contratação:'))
    dados['salario'] = float(input('Salário: R$'))
    dados['aposentadoria'] = (dados['idade'] + dados['contratação'] + 35) - datetime.now().year

print('-'*20)
for k, v in dados.items():
    print(f'{k} tem o valor {v}')