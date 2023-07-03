# DICIONÁRIOS
# Os dicionários permitem-nos substituir os índices padronizados por nomes escolhidos pelo programador.
dict = {'nome':'El Primo',
        'Classe': 'Tanque',
        'Velocidade': 'Rápido'
        }
print(dict['nome'])
print(dict['Classe'])
print(dict['Velocidade'])
print(dict)
# Podemos deletar dados e inserir novos.
del dict['Velocidade']
dict['Sexo'] = 'M'
print(dict)
print(dict['Sexo'])
# Os VALORES (Values) são todas as strings nos dicionários.
# As CHAVES (Keys) são os índices, inclusive se você tiver trocado o índice de 0, 1, 2... por nomes.
# Os items são OS VALORES E AS CHAVES.
print(dict.values())
print(dict.keys())
print(dict.items())
# Similar ao enumerate, temos:
print('Para este Brawler, temos:')
for keys, values in dict.items():
    print(f'{keys} é {values}.')
# Posso juntar lista, dicionários e tuplas.
dict2 = {'nome':'Mortis',
        'Classe': 'Assassino',
        'Sexo': '?'
        }
lista_brawling = []
lista_brawling.append([dict, dict2])
print(lista_brawling)
# Exercícios do 90 ao 95
# Decidi me dedicar, proporcionalmente, um pouco menos em dicionários.
# Fiquei 3 dias estudando listas, por querer fazê-las da melhor forma possível.
# Mas acho que esse alto nível de excelência pode não ser a estratégia mais inteligente.
# É claro que eu admiro a perseverança e a ambição desenfreada, mas talvez
# o maior desafio não seja o de completar todos os exercícios com perfeição,
# e sim o de revisá-los no longo prazo. Quer dizer, sem tentar matar o coelho hoje,
# mas emboscá-lo, com paciência.
# Até porque, mesmo que hoje eu saiba tudo que é possível sobre listas, daqui um mês
# eu já sei que minha memória não vai ser a mesma. Precisarei revisar. Ter
# um sobreaprendizado hoje não vai me dar melhores resultados na memória de longo
# prazo e isso já é bem sabido.
# Nesse caso, menos é mais. Faça um pouco menos hoje, mas repita amanhã, repita
# mês que vem. Amanhã você força mais do que hoje. Mês que vem você força mais do
# que amanhã. Então mês que vem seria o esforço máximo que tento aplicar em um único
# dia. Estudar exige um pouco de sofrimento. No final, eu tento sofrer tudo de uma
# vez para evitar repeti-lo. Não! Faça as coisas devagarinho, sem pressa.
# Eu vou ter minha chance de "lutar com todas minhas forças" nos exercícios
# que tive mais dificuldade, mas não precisa ser hoje.
