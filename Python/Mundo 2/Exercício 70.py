q = c = total = mais_barato_preco = 0
mais_barato_nome = ''
while True:
    nome = input('Qual o nome do produto? ')
    preco = float(input('Qual o preço do produto? R$ '))
    total += preco
    if q == 0 or mais_barato_preco > preco:
        mais_barato_nome = nome
        mais_barato_preco = preco
    if preco > 1000:
        c += 1
    q += 1
    condicao = input('Gostaria de continuar? S/N ').strip().upper()
    if condicao != 'S':
        break
print(f'O produto mais barato é {mais_barato_nome}. {c} custam mais de 1000 reais \n'
      f'e o total das compras é de R${total}. ')
