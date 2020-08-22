#Você pode montar o seu próprio intactive help para as funções
#que venha a criar.

#Exemplo
def prin(frase):
    """
    -> Cria uma frase estilizada e mostra na tela.
    :Entrada: Apos acionar a funcao, coloque entre aspas a frase
    :Saida: Frase estilizada
    """

    x = len(frase) + 4
    print('~'*x)
    print(f'  {frase}')
    print('~'*x)

help(prin)