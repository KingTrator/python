# O código abaixo não está funcionando. Pretendia comparar dois arquivos
# e verificar os dados que diferiam neles. Entretanto, um deles possuía
# mais colunas para verficar que o outro, e isso deveria ser considerado.
# ao fim, haveria um print do nome dos contatos e número de telefone
# daqueles que não estivessem presentes no outro arquivo (contatos_novos).
# Ao que parece, o erro é por incompatibilidade do PlanMaker como xlsx
# e o panda. Eu tratei de trocar a leitura de códivo CSV para ser uma leitura
# de excel, mas também não deu certo. Tudo, claro, com a ajuda do chatGPT.
# Ainda não cheguei nessa parte de tratamento de erros no Python, então,
# apesar de não ter conseguido executar o código, fiquei feliz pelo treinamento.
'''import pandas as pd
# Carregue os contatos da conta antiga e da nova em DataFrames do pandas
try:
    contatos_antigos = pd.read_excel('C:/Users/Win10/Downloads/contatos_antigos.xlsx', usecols=['Name', 'Phone 1 - Value', 'Phone 2 - Value', 'Phone 3 - Value'])
except ValueError:
    contatos_antigos = pd.read_excel('C:/Users/Win10/Downloads/contatos_antigos.xlsx', usecols=['Name', 'Phone 1 - Value'])

try:
    contatos_novos = pd.read_excel('C:/Users/Win10/Downloads/contatos_novos.xlsx', usecols=['Name', 'Phone 1 - Value', 'Phone 2 - Value', 'Phone 3 - Value'])
except ValueError:
    contatos_novos = pd.read_excel('C:/Users/Win10/Downloads/contatos_novos.xlsx', usecols=['Name', 'Phone 1 - Value'])
# Concatena as colunas 'Phone 1 - Value', 'Phone 2 - Value' e 'Phone 3 - Value'
contatos_antigos['Phone'] = contatos_antigos[['Phone 1 - Value', 'Phone 2 - Value', 'Phone 3 - Value']].apply(lambda x: ' '.join(x.dropna()), axis=1)

# Divide os números de telefone na primeira ocorrência de ":::" e mantém todos os números
contatos_antigos['Phone'] = contatos_antigos['Phone'].str.split(':::')

# Filtra apenas os contatos cujos números de telefone começam com "+55"
contatos_antigos = contatos_antigos[contatos_antigos['Phone'].apply(lambda x: any([num.strip().startswith('+55') for num in x]))]

# Converta os nomes dos contatos para conjuntos e encontre os nomes que estão no antigo, mas não no novo
contatos_nao_transferidos = set(contatos_antigos['Name']) - set(contatos_novos['Name'])

print("Contatos não transferidos:")
for contato in contatos_nao_transferidos:
    # Encontre o(s) número(s) de telefone para este contato no DataFrame original
    numeros = contatos_antigos[contatos_antigos['Name'] == contato]['Phone'].values[0]
    print(f'Nome: {contato}')
    for numero in numeros:
        print(f'Número: {numero.strip()}')
    print('\n') '''