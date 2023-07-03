# Exercício Python 113: Reescreva a função leiaInt() que fizemos no desafio 104, incluindo agora a
# possibilidade da digitação de um número de tipo inválido.
# Aproveite e crie também uma função leiaFloat() com a mesma funcionalidade.


def leiaint(msg):
    while True:
        try:
            m = int(input(msg))
        except (ValueError, TypeError):
            print('Digite um valor INTEIRO válido')
            continue
        else:
            return m


def leiafloat(msg):
    while True:
        try:
            m = float(input(msg))
        except (ValueError, TypeError):
            print('Digite um número fluante válido!')
            continue
        else:
            return m


num = leiaint('Digite um número inteiro: ')
print(f'Você digitou o número {num}.')
num2 = leiafloat('Digite um número fluante: ')
print(f'Você digitou o número {num2}')
