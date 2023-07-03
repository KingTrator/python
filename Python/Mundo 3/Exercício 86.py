# Exercício Python 086: Crie um programa que declare uma matriz de
# dimensão 3×3 e preencha com valores lidos pelo teclado.
# No final, mostre a matriz na tela, com a formatação correta.

# É possível tornar o programa mais eficiente, generalista e curto:
matriz = [[0, 0, 0], [0, 0, 0], [0, 0, 0]]
tam = 0
for i in range(len(matriz)):
    for j in range(len(matriz[i])):
        matriz[i][j] = float(input(f'Digite um valor para a posição {i}{j}: '))
        tam = max(tam, len(str(matriz[i][j])))  # Atualiza tam para ser o maior número de dígitos.
for i in range(3):
    for j in range(3):
        print(f'[{matriz[i][j]:^{tam}}]', end=' ')
    print()
# Obs: O erro que está sendo apontado pelo Pycharm é, provavelmente, um falso positivo, pois o script funciona
# perfeitamente.
# Programa antigo
temp = []
print('Monte uma matriz.')
for i in range(1, 10):
    num = float(input(f'Digite os valores da matriz: '))
    temp.append(num)
c = 0
m = len(str(max(temp)))   # um detalhe que enriquece o exercício
print('\033[1;4;33mMATRIZ FORMATADA\033[m')
print(' ' * 10, end='')
for i in temp:
    if c < 3:
        print(f'[{i:^{m}}]', end='')
        c += 1
    elif c == 3:
        print()
        print(' ' * 10, end='')
        print(f'[{i:^{m}}]', end='')
        c = 1
