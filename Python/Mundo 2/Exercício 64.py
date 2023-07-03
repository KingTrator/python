N = 0
c = 0
M = 0
S = 0
print('Caso queira parar de fazer as somas, digite 999.')
while N != 999:
    N = int(input('Digite um número para a soma: '))
    S += N
    c += 1
    if N == 999:
        print(f'A soma dos números é {S} e ao todo foram digitados'
              f'{c} números ou {c - 1} desconsiderando-se o 999. '
              f'\nDesconsiderando-se o 999, teríamos {S - 999}.')
    if c % 20 == 0:
        print('Lembrete: caso queirar parar, digite 999.')
print('FIM')
