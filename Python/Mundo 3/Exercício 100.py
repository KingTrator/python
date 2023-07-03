from random import randint
from time import sleep
# Exercício Python 100: Faça um programa que tenha uma lista
# chamada números e duas funções chamadas sorteia() e somaPar().
# A primeira função vai sortear 5 números e vai colocá-los dentro
# da lista e a segunda função vai mostrar a soma
# entre todos os valores pares sorteados pela função anterior.

numeros = []


def sorteia(lista):
    print(f'Sorteando valores:', end=' ')
    for i in range(5):
        n = randint(1, 5)
        print(n, end='|')
        sleep(0.5)
        lista.append(n)
    print()
    print('-='*30)
    print(f'\033[1;33mA lista dos valores sorteados é:\033[m {lista}')
    print('-='*30)


def somapar(lista):
    spar = list()
    m = 0
    for i, v in enumerate(lista):
        if v % 2 == 0:
            spar.append(v)
            m += v
    print(f'\033[1;32mA lista dos pares é: \033[m{spar}')
    print(f'\033[1;32mA soma dos valores pares é \033[m{m}')


sorteia(numeros)
somapar(numeros)

# lista = [1, 3, 6, 6, 8]
# somapar(lista)
# Os comentáriso de cima, caso permita-lhes que entrem no programa,
# provam que agora a somapar() é uma função independente de sorteia().
# Portanto, sempre que eu quiser a soma de números pares de uma lista
# que contenha apenas números, posso usá-la.