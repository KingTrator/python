# Exercício Python 085: Crie um programa no qual o usuário possa
# digitar sete valores OK
# numéricos e cadastre-os em uma lista única OK
# que mantenha separados os valores pares e ímpares. OK
# No final, mostre os valores pares e ímpares em ordem crescente. OK
lista = [[], []]
for i in range(7):
    num = int(input('Digite um número inteiro: '))
    if num % 2 == 0:
        lista[0].append(num)
    else:
        lista[1].append(num)
lista[0].sort()
lista[1].sort()
print(lista)
