from random import randint
from time import sleep
from operator import itemgetter

jogo = {'jogador1' : randint(1, 6),
        'jogador2' : randint(1, 6),
        'Jogador3' : randint(1, 6),
        'jogador4' : randint(1, 6)}

ranking = []

print('Valores Sorteados:')
for k, v in jogo.items():
    print(f'{k} tirou {v} no dado.')
    sleep(1)

ranking = sorted(jogo.items(), key=itemgetter(1), reverse=True) #Colocar em Ordem Reversa!

print('-'*27)
print('  Ranking dos Jogadores')
for i, v in enumerate(ranking):
    print(f'{i+1}° lugar: {v[0]} com {v[1]}.')