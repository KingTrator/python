# Exercício Python 093: Crie um programa que gerencie o
# aproveitamento de um jogador de futebol. O programa vai ler
# o nome do jogador e quantas partidas ele jogou.
# Depois vai ler a quantidade de gols feitos em cada partida.
# No final, tudo isso será guardado em um dicionário,
# incluindo o total de gols feitos durante o campeonato.
dados = dict()
dados['nome'] = input('Nome: ')
dados['partidas'] = int(input('Partidas: '))
gols = []
total_gols = 0
for i in range(dados['partidas']):
    gols_partida = int(input(f'Gols na {i+1}ª partida: '))
    gols.append(gols_partida)
    total_gols += gols_partida
dados['gols'] = gols
dados['total'] = total_gols
print(dados['nome'], 'teve o seguinte desempenho: ')
for i, gol in enumerate(dados['gols']):
    print(f'Na {i+1}ª partida: {gol} gols.')
print(dados['nome'], f'fez ao todo {total_gols} gols.')
