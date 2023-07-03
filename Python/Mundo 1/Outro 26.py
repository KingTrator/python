# Resolvendo o exercício sem if-else.
#1
cidade = input('\033[1;4;33mDigite o nome da cidade:\033[m ').strip()
analisar = cidade.split()
santo = analisar[0]
f = santo.upper() # Código à prova de burros LOL
x = f.find('SANTO')
print('{}Para a palavra Santo em {}, em relação a '
      'ser ou não prefixo, temos: {}.{}'.format('\033[1;4;33m', cidade, x, '\033[m'))
print('\033[1;4;33mO = verdadeiro. -1 = falso.\033[m')
#2
nome = input('\033[1;37mDigite o seu nome: \033[m')
x = nome.upper() # eu adicionei essa linha de código para o caso de o usuário digiitar Silva com varições entre maiúsculas e minúsculas.ds
y = x.find('SILVA')
print('\033[1;4;33mO nome {}, retorna para o sobrenome Silva: {}.\033[m'.format(nome, y))


# Se eu escrever uma palavra compostas e ela não estivar em uma lista [ ], a qual
# pode ser obtida por meio de nome.split, que irá fragmentar a construção frasa
# com referencial nos espaços, (ABD DED) = 2 índices, mas (ABDDED) é só um, o espaço
# fragmenta, eu terei -1 ou 0 de retorno. Se eu pôr ela numa lista (acredito), aí
# sim eu terei o retorno da posição em que ela está, 0, 1, 2, 3...

# Na verdade, "achar" Silva significava dizer se é True ou False o Silva. ENTÃO
# Vou refazer o exercício:
agarra = input('\033[1mDigite seu nome completo:\033[m ')
lol = agarra.upper()
print('\033[1m Olá! Percebo que SILVA é {} no seu nome completo.\033m'.format('SILVA' in lol))
