# Exercício Python 101: Crie um programa que tenha uma função chamada
# voto() que vai receber como parâmetro o ano de nascimento de uma pessoa,
# retornando um valor literal indicando se uma pessoa tem voto
# NEGADO, OPCIONAL e OBRIGATÓRIO nas eleições.


def voto(year):
    from datetime import datetime   # é melhor importar dentro da função, isso economiza memória, pois a função
    ano = datetime.now().year       # só será usada dentro desta função.
    if ano - year < 16:
        print(f'Com {ano - year} anos: NÃO VOTA.')
    elif 16 <= (ano - year) < 18 or 65 <= (ano - year):
        print(f'Com {ano - year} anos: VOTO OPCIONAL.')
    else:
        print(f'Com {ano - year} anos: VOTO OBRIGATÓRIO.')


n = int(input('Em que ano você nasceu? '))
voto(n)  # Como eu fiz voto(year) em vez de apenas um "voto", posso testar livremente a função. É melhor
         # do que deixar o input dentro do código.
