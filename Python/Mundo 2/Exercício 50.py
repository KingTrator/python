from math import trunc
s = 0
for i in range(1, 7):
    n = float(input('Digite um número inteiro para verificar a soma dos pares: '))
    k = n/2
    if trunc(k) == k:
        s = s + n
if s == 0:
    print('Ou você não digitou algum inteiro, ou digitou apenas ímpares.')
else:
    print('A soma do total de inteiros PARES que você digitou é {}'.format(s))
