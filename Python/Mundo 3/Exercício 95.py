# Exercício Python 095: Aprimore o desafio 93 para que ele
# funcione com vários jogadores, incluindo um sistema de
# visualização de detalhes do aproveitamento de cada jogador.
time = []
jogador = dict()
partidas = list()
while True:
    jogador.clear()
    jogador['nome'] = input('Nome: ')
    tot = int(input('Partidas jogadas: '))
    partidas.clear()
    for c in range(0, tot):
        partidas.append(int(input(f'Gols na partida {c+1}: ')))
    jogador['gols'] = partidas[:]
    jogador['total'] = sum(partidas)
    time.append(jogador.copy())
    while True:
        resp = str(input('Quer continuar? S/N ')).upper()[0]
        if resp in 'SN':
            break
        print('Responda S ou N.')
    if resp == 'N':
        break
print('-='*30)
print('cod', end='')
for i in jogador.keys():
    print(f'{i:<30}', end='')
print('-='*40)
for k, v in enumerate(time):
    print(f'{k:>3}', end=' ')
    for d in v.values():
        print(f'{str(d):<30}', end='')
    print()
print('-='*40)
while True:
    busca = int(input('Digitar dados de qual jogador? (999 para PARAR) '))
    if busca == 999:
        break
    if busca >= len(time):
        print(f'ERRO! Não existe jogador com índice {busca}')
    else:
        print(f'LEVANTAMENTO DO JOGADOR {time[busca]["nome"]}')
        for i, g in enumerate(time[busca]['gols']):
            print(f'    Na partida {i+1}ª = {g} gols.')
    print('-='*40)