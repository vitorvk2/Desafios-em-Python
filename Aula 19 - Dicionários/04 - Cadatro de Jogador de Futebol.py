jogador = {}
partidas = []
jogador['nome'] = str(input('Nome do Jogador:'))
tot = int(input(f'Quantas partidas o {jogador["nome"]} jogou?'))

for c in range(0, tot):
    partidas.append(int(input(f'Quantos gols na partida {c}?')))
jogador['gols'] = partidas[:]
jogador['total'] = sum(partidas)

for i, v in enumerate(jogador['gols']):
    print(f' => Na partida {i}, ele fez {v} gols.')
print(f'Foi um total de {jogador["total"]} gols')