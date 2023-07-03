# Ler 5 valores e guarde-os em uma lista. OK
# Mostrar maior e menor.
# Dizer a posição do maior e do menor.
maior = menor = 0
a = []
for i in range(5):
    a.append(int(input('Digite um número: ')))  # Não sabia que dava para fazer isto.
    if i == 0:
        maior = menor = a[i]
    else:
        if maior < a[i]:
            maior = a[i]
        if menor > a[i]:
            menor = a[i]
print(f'A lista é {a}.')
print(f'O maior valor da lista é {maior}, encontrado nas posições:', end=' ')
for i, v in enumerate(a):
    if maior == v:
        print(f'{i},', end=' ')
print('')
print(f'O menor valor da lista é {menor}, encontrado nas posições: ', end=' ')
for i, v in enumerate(a):
    if menor == v:
        print(f'{i},', end=' ')
