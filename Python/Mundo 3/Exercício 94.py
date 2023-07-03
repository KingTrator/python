# Exercício Python 094: Crie um programa que leia nome,
# sexo e idade de várias pessoas, guardando os dados de cada pessoa
# em um dicionário e todos os dicionários em uma lista. No final, mostre:
# A) Quantas pessoas foram cadastradas  OK
# B) A média de idade   OK
# C) Uma lista com as mulheres  OK
# D) Uma lista de pessoas com idade acima da média  OK
dados = {}
lista = []
c = m = 0
while True:
    dados['Nome'] = input('Nome: ').strip()
    dados['Sexo'] = input('Sexo M/F: ').upper().strip()
    dados['Idade'] = int(input('Idade: '))
    m += dados['Idade']
    lista.append(dados.copy())
    del dados
    dados = {}
    c += 1
    ask = input('Gostaria de parar? S/N ').upper()[0]
    if ask in 'Ss':
        break
lista_mulheres = []
for i in range(len(lista)):
    if lista[i]['Sexo'] in 'Ff':
        lista_mulheres.append(lista[i])
pessoas_velhas = []
for i in range(len(lista)):
    if lista[i]['Idade'] > m/c:
        pessoas_velhas.append(lista[i]['Nome'])
print('\033[1;33m-='*3, 'DADOS CADASTRADOS', '-=\033[m'*3)
print('  '*3, '\033[1mDADOS GERAIS\033[m')
for i in range(len(lista)):
    print(lista[i])
    print('-='*30)
print('  '*3, '\033[1mDADOS ESPECÍFICOS\033[m')
print('-='*3,'\033[1;32mMULHERES CADASTRADAS:\033[m', '-='*3)
for i, v in enumerate(lista_mulheres):
    print(f'{lista_mulheres[i]}')
    print('-='*30)
print('-='*3, '\033[1;32mPESSOAS MAIS VELHAS:\033[m', '-='*3)
for i in range(len(pessoas_velhas)):
    print(pessoas_velhas[i])
    print('-='*30)
print('-='*3, '\033[1;31m OUTROS DADOS ESPECÍFICOS:\033[m', '-='*3)
print(f'A média das idades foi {m/c:.2f}')
print(f'Ao todo, {c} pessoas foram cadastradas.')

# Há um jeito de simplificar o código. O GPT-4 já o apontou.
# Mais tarde eu volto para fazer isso.
