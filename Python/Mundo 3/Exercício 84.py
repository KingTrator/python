# Exercício Python 084: Faça um programa que leia o nome e o peso de
# várias pessoas, guardando tudo em uma lista. No final, mostre:
# A) Quantas pessoas foram cadastradas. OK
# B) Uma listagem com as pessoas mais pesadas. OK
# C) Uma listagem com as pessoas mais leves. OK
c = 0  # contador de pessoas adicionados, assim como break activator.
dados = []  # Define a lista com todos os nomes
maior_peso = menor_peso = 0
pesadas = []
leves = []
while True:
    nome = input('Nome da pessoa: ')
    np = int(input('Peso da pessoa: '))
    dados.append([nome, np])
    c += 1
    if c == 1 or np > maior_peso:
        pesadas = [nome, np]
    elif np == maior_peso:  # Só adicionamos à pesadas aqueles de mesmo peso, para a lista não ficar gigante.
        pesadas.append([nome, np])
    if c == 1 or np < menor_peso:
        leves = [nome, np]
    elif np == menor_peso:
        leves.append([nome, np])
    if c == 4 or nome == '':
        question = input('Gostaria de parar de adicionar nomes? ')
        if question in 'Ss':
            break
print(f'{c} pessoas foram adicionadas à lista.')
print(f'Dessasm {pesadas} são as mais pesadas.')
print(f'Por outro lado, {leves} são as mais leves.')

# Eu poderia ter adicionado mais linhas de código para fazer com que houvesse um limite em
# "pesadas" e "leves", deletando os valores mais antigos caso "c" ultrapaasse um determinado valor.
# Mas acho que do modo que está, o exercício já está realizado.
# OUTRA POSSIBILIDADE DE RESOLUÇÃO:
heavy = light = 0
principal = []
temp = []
while True:
    temp.append(input('Digite seu nome: '))
    temp.append(float(input('Digite seu peso: ')))
    if len(principal) == 1:
        heavy = light = temp[1]
    else:
        if heavy < temp[1]:
            heavy = temp[1]
        if light > temp[1]:
            light = temp[1]
    principal.append(temp[:])
    temp.clear()
    ask = input('Quer parar? S/N ')
    if ask in 'Ss':
        break
print(f'O total de pessoas adicionadas foi de {len(principal)}')
print(f'O maior peso foi de {heavy}, presente em: ', end='')
for i in principal:
    if heavy == i[1]:  # for i in significa: para os índices dentro de principal.
        print(f'{i[0]} ')
print('')
print(f'O menor peso foi de {light}, presente em: ', end='')
for i in principal:   # como o índice mostra uma sublista e não um int, eu devo fazer assim mesmo.
    if light == i[1]:
        print(f'{i[0]} ', end='')

