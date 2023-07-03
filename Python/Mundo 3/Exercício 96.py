# Exercício Python 096: Faça um programa que tenha uma função chamada
# area(), que receba as dimensões de um terreno retangular
# (largura e comprimento) e mostre a área do terreno.


def area(ll, b):
    print(f'A área do terreno retangular de dimensões: {ll, b} = ', end='')
    print(f'{ll * b}m²')


a = float(input('Largura do terreno: '))
c = float(input('Comprimento do terreno: '))
area(a, c)
