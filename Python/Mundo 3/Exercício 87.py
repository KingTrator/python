#Exercício Python 087: Aprimore o desafio anterior, mostrando no final:
# A) A soma de todos os valores pares digitados.
# B) A soma dos valores da terceira coluna.
# C) O maior valor da segunda linha.
matriz = [[0, 0, 0], [0, 0, 0], [0, 0, 0]]
tam = contador = conto = 0
print('__'*30)
print('\033[1;33mMATRIZ 3X3 DE NÚMEROS INTEIROS\033[m'.center(65))
print('__'*30)
for i in range(0, 3):
    for j in range(0, 3):
        num = int(input(f'Escolha um valor para o elemento {i}|{j}: '))
        matriz[i][j] = num
        tam = max(tam, len(str(num)))  # o maior valor a ser digitado é salvo em tam para delimitar a formatação.
        if num % 2 == 0:
            contador += num  # salva os números pares
        if j == 2:
            conto += num  # salva o último número da sublista, que, no caso, são os elementos da coluna 3.
print(' '*20, '\033[1;33mMATRIZ\033[m')
print('__'*30)
for i in range(0, 3):
    for j in range(0, 3):
        print(f'[{matriz[i][j]:^{tam}}]', end=' ')
    print()
print('__'*30)
print(f'A soma dos valores pares digitados é = {contador}.')
print(f'A soma dos valores da terceira coluna é = {conto}.')
max_value = max(matriz[1])
print(f'O maior valor da segunda linha é = {max_value}')
print('__'*30)
