from random import randint
from time import sleep
from operator import itemgetter  # função nova.
# Exercício Python 091: Crie um programa no qual 4 jogadores joguem um
# dado e tenham resultados aleatórios. Guarde esses resultados em um
# dicionário em Python. No final, coloque esse dicionário em ordem,
# sabendo que o vencedor tirou o maior número no dado.
jogo = dict()
print('-='*3, '\033[1;33mSORTEIO\033[m', '-='*3)
for i in range(4):
    jogo[f'jogador {i+1}'] = randint(1, 6)
for key, values in jogo.items():
    print(f'{key} tirou {values}')
    sleep(0.5)
ranking = sorted(jogo.items(), key=itemgetter(1), reverse=True)
print('-='*3, '\033[1;33mRESULTADOS\033[m', '-='*3)
for indices, valores in enumerate(ranking):
    print(f'{valores[0]} em {indices+1}º lugar')
    sleep(0.5)
# Esse código não considera igualar a posição dos jogadores que tiram a mesma pontuação.
# No entanto, como o próprio professor não fez essa correção, também deixarei passar.