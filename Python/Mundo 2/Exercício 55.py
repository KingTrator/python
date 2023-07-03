maior_peso = 0
menor_peso = 999**9999 #  Caso o menor peso fosse o primeiro a ser registrado, ele não seria

for i in range(5):
    p = float(input('Digite o seu peso em Kg: '))
    if p > maior_peso:
        maior_peso = p
    if menor_peso > p: #  Aqui eu devo usar o if e não elif ou else, pois uma condição não implica negar outra.
        menor_peso = p

if menor_peso == maior_peso:
    print(f'Pesos iguais foram repetidos 5 vezes, a saber {maior_peso}.')
else:
    print(f'O maior peso foi {maior_peso} e o menor peso foi {menor_peso}')

# Consegui! Depois de resolver o Exercício 56 com auxílio do GPT-4, saquei
# qual era a ideia a ser desenvolvida aqui e desenvolvi um código limpo e correto.
