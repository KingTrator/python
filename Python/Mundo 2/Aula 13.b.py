# Continuação da aula 13
for i in range(1, 4):
    n = int(input('Digite um número: '))
# Outro exemplo:
a = int(input('Escolha quantas vezes quer que o looping acontença: '))
# definindo a lista que armazenará as entradas.
numeros = []
for i in range(a):
    num = int(input('Digite um número'))
    # Em ordem, o que é digitado em "num" é adicionado à lista numeros.
    numeros.append(num)
print('O primeiro número que você digitou foi {}'
      ' e o último {}'.format(numeros[0], numeros[a-1]))
# Note que foi preciso escrever numeros[a-1] porque não existe na lista o item
# "5", pois uma lista de 5 itens é representada por: 0, 1, 2, 3, 4.
print('FIM')

# Exercícios do 46 ao 56