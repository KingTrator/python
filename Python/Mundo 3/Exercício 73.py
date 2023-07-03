a = ('Botafogo', 'Palmeiras', 'Fluminense', 'Atlético', 'Cruzeiro', 'Atlético', 'São Paulo', 'Santos', 'Flamengo', 'Fortaleza', 'Bragantino', 'Grêmio', 'Bahia',
     'Internacional', 'Goiás', 'Vasco', 'Corinthians', 'Cuiabá', 'América', 'Coritiba')
print(f'Listas dos times da série A {a}.')
print(f'Os 5 primeiros são {a[0]}, {a[1]}, {a[2]}, {a[3]}, {a[4]}')
print(f'Os 4 últimos são: {a[-1]}, {a[-2]}, {a[-3]}, {a[-4]}. ')
print(f'Os times em ordem alfabética: {sorted(a)}.')
print(f'A posição do Fluminense é {a.index("Fluminense") + 1}ª.')  # Se você usar aspas simples para a f'string
#                                                             # deverá usar duplas dentro dela e vice-versa.
