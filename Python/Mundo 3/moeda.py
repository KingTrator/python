def resumov(m):
    print(f'-='*20)
    print('\033[1mRESUMO DO VALOR\033[m'.center(45))
    print(f'-='*20)
    print(f'1,1 x {m} = {aumentar(m)} \n'
          f'0,9 x {m} = {diminuir(m)} \n'
          f'{m} / 2 = {metade(m)} \n'
          f'2 x {m} = {dobro(m)}')
    print(f'-='*20)


def moeda(m, neutral=False):
    z = f'R${m:.2f}'.replace('.', ',')
    return z if not neutral else m


def aumentar(m, neutral=False):
    z = 1.1 * m
    return moeda(z) if not neutral else z


def diminuir(m, neutral=False):
    z = 0.9 * m
    return moeda(z) if not neutral else z


def metade(m, neutral=False):
    z = m / 2
    return moeda(z) if not neutral else z


def dobro(m, neutral=False):
    z = m * 2
    return moeda(z) if not neutral else z
