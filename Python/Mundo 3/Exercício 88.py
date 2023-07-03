from random import randint
# Exercício Python 088: Faça um programa que ajude um jogador da
# MEGA SENA a criar palpites.
# O programa vai perguntar quantos jogos serão gerados  OK
# E vai sortear 6 números entre 1 e 60 para cada jogo OK
# Cadastrando tudo em uma lista composta. OK
ask = int(input('Quantos jogos você gostaria de sortear? '))
tot = 0
lista = list()
cont = 0
jogos_lista = []
while tot < ask:
    while True:
        num = randint(1, 60)
        if num not in lista:
            lista.append(num)
            cont += 1
        if cont >= 6:
            tot += 1
            lista.sort()
            jogos_lista.append(lista[:])
            lista.clear()
            cont = 0
            break
print('-='*4, '\033[1;33mLISTA DE JOGOS\033[m', '-='*5)
for i, j in enumerate(jogos_lista):
    print(f'Jogo {i+1}: {j}')
print('-='*5, '\033[1;33mBOA SORTE!\033[m', '-='*5)
