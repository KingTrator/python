# Exercício Python 102: Crie um programa que tenha uma função
# fatorial() que receba dois parâmetros: o primeiro que indique o
# número a calcular e outro chamado show, que será um valor lógico (opcional) indicando se
# será mostrado ou não na tela o processo de cálculo do fatorial.


def fatorial(n, show=False):
    '''

    :param n: calcula o fatorial de n
    :param show: opcional, se True, mostra a conta
    :return: Nada
    '''
    m = 1
    conta = list()
    for i in range(n):
        m *= (n - i)
        conta.append(n-i)
    if show is True:
        for i, v in enumerate(conta):
            if conta[i] != conta[-1]:       # não pode fazer v[i], porque v é o valor (identidade) e
                print(f'{v} x ', end='')    # não o elemento da lista (identidade)
            else:
                print(f'{v} = {m}')
    else:
        print(m)


fatorial(6, True)
help(fatorial)
# tente refazer esta função, mas em vez de "for i in range(n)" use for i in range(n, 0, -1)
