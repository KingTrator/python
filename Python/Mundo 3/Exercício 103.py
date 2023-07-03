# Exercício Python 103: Faça um programa que tenha uma função chamada
# ficha(), que receba dois parâmetros opcionais: o nome de um jogador e
# quantos gols ele marcou. O programa deverá ser capaz de mostrar a ficha
# do jogador, mesmo que algum dado não tenha sido informado corretamente.


def ficha(n='<unkown>', b=0):
    print(f'O jogador {n} fez {b} gol(s) no campeonato.')


nome = str(input('Nome do jogador: '))
gols = str(input('Nome do jogador: '))
if gols.isnumeric():
    gols = int(gols)
else:
    gols = 0
if nome.strip == '':
    ficha(b=gols)
else:
    ficha(nome, gols)
