print('='*10,'Loja do Vitor','='*10)
com = float(input('Digite o valor das compras:'))
p = int(input('''FORMAS DE PAGAMENTO
[ 1 ] à vista dinheiro/cheque
[ 2 ] à vista no cartão
[ 3 ] 2x no cartão
[ 4 ] 3x ou mains no cartão

Qual é a opção desejada?
'''))

if p == 1:
    v = com * 0.90
    print(f'O valor do produto é R${(com):0.2f}, o valor a ser pago é: R${(v):0.2f}.')
elif p == 2:
    v = com * 0.95
    print(f'O valor do produto é R${(com):0.2f}. Em 2x, o valor a ser pago é: R${(v):0.2f}.')
elif p == 3:
    v = com/2
    print(f'O valor a ser pago é: R${(v):0.2f}.')
else:
    par = int(input('Quantas parcelas deseja pagar?'))
    v = (com * 1.20)/par
    print(f'O valor do produto é R${(com):0.2f}. Em {(par)}x, o valor a ser pago é: R${(v):0.2f} .')