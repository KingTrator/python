a = ('cachorro', 'barata', 'bobo', 'carniça', 'gentil', 'baú')
for i in a:                                        # Às vezes esqueço que posso fazer isso direto.
    print(f'{i:^10} possui as vogais: ', end=' ')  # A tradução é mais ou menos: "para cada índice da variável".
    for j in i:                                    # Isso agora faz mais sentido. Uso um looping para ver
        if j.lower() in 'aáãâéêeiíoôuú':                           # índices de outro índice.
            print(f'{j} ', end=' ')
    print('')
# Outra opção é, em vez de colocar as vogais na ordem em que aparecem, definir a ordem e colocar o número de vezes
# da ocorrência:
q = ('cachorro', 'barata', 'bobo', 'carniça', 'gentil')
for i in a:
    print(f'{i:^10} possui: ', end=' ')
    for j in 'aáãâéêeiíoôuú':  # Traduzindo: para cada índice da string 'aeiou', temos: 'resto do código da identação'.
        if j in i:
            c = i.count(j)
            print(f'{c} {j}', end=' | ')
    print('')
