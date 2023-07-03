from time import sleep
# Exercício Python 099: Faça um programa que tenha uma função
# chamada maior(), que receba vários parâmetros com valores inteiros.
# Seu programa tem que analisar todos os
# valores e dizer qual deles é o maior. # Proibido usar max() e similares.

def maior(lst):
    grande = []
    for i in range(len(lst)):
        if i == 0:
            grande.append(lst[i])
        else:
            if lst[i] > grande[0]:
                grande.append(lst[i])
                del grande[0]
    print(f'Dentre os valores {lst}...')
    sleep(1)
    print(f'...O maior valor é {grande[0]}.')

print('Olá! Digite quantos valores quiser e eu lhe direi qual deles foi o maior.')
lista = list()
while True:
    lista.append(float(input('Número: ')))
    while True:
        ask = input('Gostaria de parar? S/N ')[0]
        if ask in 'Ss':
            break
        elif ask in 'Nn':
            break
        else:
            print('Digite S ou N')
    if ask in 'Ss':
        break
maior(lista)

# O exercício está correto, mas pode ser simplificado. Quando fizer isto (no futuro), apague esta
# mensagem. Uma simplificaçõa foi dada pelo GPT-4.