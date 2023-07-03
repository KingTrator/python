from datetime import datetime
# Exercício Python 092: Crie um programa que leia nome,
# ano de nascimento e carteira de trabalho e cadastre-o (com idade) em um
# dicionário. Se por acaso a CTPS for diferente de ZERO, o dicionário
# receberá também o ano de contratação e o salário. Calcule e acrescente,
# além da idade, com quantos anos a pessoa vai se aposentar.
dados = dict()
dados['Nome'] = input('Nome: ')
dados['Sexo'] = input('Sexo M/F ')
data = int(input('Data de nascimento : '))
dados['CTPS'] = int(input('Carteira de trabalho (0 não tem): '))
if dados['CTPS'] != 0:
    dados['Ano de contratação'] = int(input('Ano de contratação: '))
    dados['Salário'] = float(input('Salário R$'))
dados['Idade'] = datetime.now().year - data
if dados['CTPS'] != 0:
    if dados['Sexo'] in 'Ff':
        dados['Sexo'] = 'Feminino'
        dados['Idade aposentadoria'] = dados['Idade'] + (dados['Ano de contratação'] + 30 - datetime.now().year)
    elif dados['Sexo'] in 'Mm':
        dados['Sexo'] = 'Masculino'
        dados['Idade aposentadoria'] = dados['Idade'] + (dados['Ano de contratação'] + 35 - datetime.now().year)
    else:
        print('Um valor inválido foi digitado para SEXO')
if dados['Sexo'] in 'Ff':
    dados['Sexo'] = 'Feminino'
elif dados['Sexo'] in 'Mm':
    dados['Sexo'] = 'Masculino'
else:
    print('Um valor inválido foi digitado para SEXO')
for keys, values in dados.items():
    print(f'{keys} = {values}')
# Há uma série de ressalvas neste código: 1º as regras de aposentadoria
# são mais dinâmicas do que o que está exposto no código.
# 2º Há uma redundância na verificação do sexo.