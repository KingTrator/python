from time import sleep
# Exercício Python 098: Faça um programa que tenha uma função chamada contador(), que
# receba três parâmetros: início, fim e passo. Seu programa tem que realizar três
# contagens por meio da função criada:
# a) de 1 até 10, de 1 em 1
# b) de 10 até 0, de 2 em 2
# c) uma contagem personalizada


def contador(a, b, c):      # a = início, b = fim, c = passo.
    for i in range(1, 11):
        print(i, end='|')
        sleep(0.2)
    print()
    for i in range(10, 0, -1):
        print(i, end='|')
        sleep(0.2)
    print()
    if c < 0:
        print('O passo deverá ser p > 0.')
    else:
        if a < b:
            for i in range(a, b+1, c):
                print(i, end='|')
                sleep(0.2)
        else:
            for i in range(a, b-1, -c):
                print(i, end='|')
                sleep(0.2)


n1 = int(input('N1: '))
n2 = int(input('N2: '))
p = int(input('Passo (P > 0): '))

contador(n1, n2, p)
