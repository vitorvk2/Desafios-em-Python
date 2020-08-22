from datetime import date
atual = date.today().year
nasc = int(input('Ano de Nascimento:'))
idade = atual - nasc
print(f'Você nasceu em {(nasc)} e tem {(idade)} anos em {(atual)}')

if idade == 18:
    print('Você precisa se alistar IMEDIATAMENTE!')
elif idade < 18:
    sal = 18 - idade
    at = atual + sal
    print(f'Ainda faltam {(sal)} anos para o alistamento.\nSeu alistamento será em {(at)}.')

elif idade > 18:
    sal = idade - 18
    at = atual - sal
    print(f'Seu alistamento foi em {(at)}.')
