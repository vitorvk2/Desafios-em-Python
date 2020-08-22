def área(largura,comprimento):
    a = largura*comprimento
    print(f'A ária de um terreno {largura}x{comprimento} é de {a}')


print('Controle de Terrenos')
print('-'*20)
largura = float(input('Largura:'))
comprimento = float(input('Comprimento:'))
área(largura,comprimento)