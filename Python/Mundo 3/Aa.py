def fatorial(n):
    if n >= 0:
        f = 1
        for i in range(1, n+1):
            f *= i
        return f
    else:
        f = 'Valor não permitido (valor >= 0)'
        return f


def dobro(n):
    d = n * 2
    return d


def triplo(n):
    d = n * 3
    return d