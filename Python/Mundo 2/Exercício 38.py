print('Este script serve para comparar 3 números inteiros.')
n1 = int(input('Digite um número inteiro: '))
n2 = int(input('Digite um número inteiro: '))
n3 = int(input('Digite um número inteiro: '))
if n1 == n2 == n3:
    print('Os três tem o mesmo tamanho unitário')
else:
    if n1 >= n2 and n1 >= n3:
        maior = n1
    elif n2 > n1 and n2 >= n3:
        maior = n2
    else:
        maior = n3
    if n1 <= n2 and n1 <= n3:
        menor = n1
    elif n2 < n1 and n2 <= n3:
        menor = n2
    else:
        menor = n3
    print('{} É o maior dos números e {} o menor deles.'.format(maior, menor))
