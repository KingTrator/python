def resumov(m):
    print(f'-='*20)
    print('\033[1mRESUMO DO VALOR\033[m'.center(45))
    print(f'-='*20)
    print(f'1,1 x {moeda(m)} = {aumentar(m)} \n'
          f'0,9 x {moeda(m)} = {diminuir(m)} \n'
          f'{moeda(m)} / 2 = {metade(m)} \n'
          f'2 x {moeda(m)} = {dobro(m)}')
    print(f'-='*20)


def moeda(m):
    z = f'R${m:.2f}'.replace('.', ',')
    return z


def aumentar(m):
    z = 1.1 * m
    return moeda(z)


def diminuir(m):
    z = 0.9 * m
    return moeda(z)


def metade(m):
    z = m / 2
    return moeda(z)


def dobro(m):
    z = m * 2
    return moeda(z)
