# Faça um programa que leia um número de um a 5 e o escreva por extenso.
a = ('um', 'dois', 'três', 'quatro', 'cinco', 'seis', 'sete', 'oito', 'nove', 'dez', 'onze', 'doze',
    'treze', 'quatorze', 'quinze', 'dezesseis', 'dezessete', 'dezoito', 'dezenove', 'vinte',)
n = int(input('Digite um número de 1 a 5: '))
if 1 <= n <= 20:
    print(a[n-1])
else:
    print('Por favor, digite um valor válido.')
