def leiadinheiro(m):
    val = False
    while not val:
        x = str(input(m)).replace(',', '.')
        if x.isalpha():
            print(f'\033[1;31mERRO! "{x}" não é um valor válido!\033[m')
        else:
            val = True
            return float(x)



def resumov(m):
    print(f'-='*20)
    print('\033[1mRESUMO DO VALOR\033[m'.center(45))
    print(f'-='*20)
    print(f'1,1 x {m} = {aumentar(m)} \n'
          f'0,9 x {m} = {diminuir(m)} \n'
          f'{m} / 2 = {metade(m)} \n'
          f'2 x {m} = {dobro(m)}')
    print(f'-='*20)


def aumentar(m):
    z = 1.1 * m
    return f'{z:.2f}'


def diminuir(m):
    z = 0.9 * m
    return f'{z:.2f}'


def metade(m):
    z = m / 2
    return f'{z:.2f}'


def dobro(m):
    z = m * 2
    return f'{z:.2f}'
