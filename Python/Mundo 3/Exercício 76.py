print('_'*40)
a = 'LISTAGEM DE PREÇOS'
print(f'\033[1m{a:^40}\033[m')
print('_'*40)
p = ('Lápis', 0.50, 'Caneta', 2.00, 'Mochila', 150.00, 'Garrafa', 50.00,
     'Livro', 180.00)
c = 0
for i in range(len(p)//2):
    preco = (f'R${p[c + 1]:.2f}')  # Neste caso, a dupla formatação é desnecessária
    print(f'{p[c]:^10}', '_' * 20, f' {preco:^4}')  # bastaria usar :.2f aqui.
    c += 2                         # Mas fica de lembrete.
print('_'*40)
