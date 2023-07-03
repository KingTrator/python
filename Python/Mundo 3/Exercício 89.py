# Exercício Python 089: Crie um programa que
# leia nome e duas notas de vários alunos OK
# e guarde tudo em uma lista composta. OK
# No final, mostre um boletim contendo a média de cada um OK
# e permita que o usuário possa mostrar as notas de cada aluno
# individualmente. OK
compostas = list()
while True:
    nome = input('Digite o nome do aluno: ')
    n1 = float(input('Digite a primeira nota dele: '))
    n2 = float(input('Digite a segunda nota dele: '))
    compostas.append([nome, n1, n2])
    ask = input('Quer continuar? S/N ')
    if ask in 'Nn':
        break

for i in range(len(compostas)):
    media = (compostas[i][1] + compostas[i][2]) / 2
    compostas[i].insert(3, [media])
n = 1
for i in compostas:
    print('No.','-='*15, 'Média' )
    print(f'{i[0]}, aluno número {n}º,  obteve média: {i[3]}')  # Isso é só firula, mas deixa o código menos
    print('__'*20)                                              # eficiente para leitura.
    n += 1
while True:
    question = int(input('Gostaria de ver as notas de quais alunos? 999 para encerrar '))
    if question != 999:
        if 1 <= question <= len(compostas):
            print(f'{compostas[question-1][1]} e {compostas[question-1][2]}')
        else:
            print('Oops! Você digitou uma opção inválida. Tente novamente.')
    if question == 999:
        print('Programa encerrado')
        break
# Existe uma versão simplificada deste (ou do exercício 88) que eu quero fazer também.
