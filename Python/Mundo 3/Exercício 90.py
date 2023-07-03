# Exercício Python 090: Faça um programa que leia nome e média de um aluno,
# guardando também a situação em um dicionário.
# No final, mostre o conteúdo da estrutura na tela.
dados = dict()
dados['nome'] = str(input('Nome: '))
dados['média'] = float(input(f'Média de {dados["nome"]} '))
if 10 >= dados['média'] >= 7:
    print('Aprovado!')
    print(dados)
elif 0 <= dados['média'] < 7:
    print('Reprovado!')
    print(dados)
else:
    print('Por favor, digite um valor válido para MÉDIA (0 a 10).')
