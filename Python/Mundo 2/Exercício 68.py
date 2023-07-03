from random import randint
print('JOGO DE PAR OU ÍMPAR')
print('Para jogar a favor do PAR, digite P. Para jogar a favor do ÍMPAR digite I.')
b = a = c = 0
contador = 0
while True:
    c = input('Você quer PAR ou ÍMPAR? P/I ').strip().upper()
    a = int(input('Escolha um número de 0 a 10: '))
    if a > 10 or a < 0:
        print('Eu disse de 1 a 10.')
        break
    b = randint(1, 11)
    if (c == 'I' and a % 2 == 0 and b % 2 == 0) or \
        (c == 'I' and a % 2 != 0 and b % 2 != 0) or \
        (c == 'P' and a % 2 != 0 and b % 2 == 0) or \
        (c == 'P' and a % 2 == 0 and b % 2 != 0):
        print(f'O computador ganhou. Antes disso, você ganhou {contador} vezes.')
        break
    if c != 'P' and c != 'I':
        break
    contador += 1
