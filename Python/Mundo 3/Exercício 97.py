# Exercício Python 097: Faça um programa que tenha uma função
# chamada escreva(), que receba um texto qualquer como
# parâmetro e mostre uma mensagem com tamanho adaptável.


def escreva(msg):
    print(f'\033[1;33m{"MENSAGEM FORMATADA":^{len(msg)*2}}\033[m')
    print(f'-='*len(msg))
    print(f'{msg:^{len(msg)*2}}')
    print(f'-='*len(msg))

while True:
    m = input('Digite uma mensagem: ')
    escreva(m)
    ask = input('Gostaria de escrever outra mensagem? S/N ')[0]
    if ask in 'Nn':
        break