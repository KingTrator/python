# Exercício Python 082: Crie um programa que vai ler vários números e
# colocar em uma lista (OK). Depois disso, crie duas listas extras que vão conter
# apenas os valores pares e os valores ímpares digitados, respectivamente.
# Ao final, mostre o conteúdo das três listas geradas.
num = list()
while True:
    num.append(int(input('Digite um número: ')))
    question = input('Gostaria de sair? S/N ')
    if question in 'Ss':
        break
pares = []
impares = []
for i in range(len(num)):
    if num[i] % 2 == 0 and num[i] >= 0:
        pares.append(num[i])
    elif num[i] >= 0:
        impares.append(num[i])
print(f'A lista com todos os números é {num}.')
print(f'A lista dos valores pares é {pares}')
print(f'A lista dos valores ímpares é {impares}')
