# Exercício Python 104: Crie um programa que tenha a função leiaInt(), que vai
# funcionar de forma semelhante ‘a função input() do Python, só que fazendo a
# validação para aceitar apenas um valor numérico.
# Ex: n = leiaInt(‘Digite um n: ‘)

def leiaint(msg):
    while True:
        m = input(msg)
        if m.isnumeric():
            valor = int(m)
            return valor
        else:
            print('\033[1;31mERRO! Digite um valor inteiro válido.\033[m')


n = leiaint('Digite um número: ')
print(f'Você digitou {n}.')
