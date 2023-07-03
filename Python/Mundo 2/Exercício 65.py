soma = maior = menor = num = contador = 0
R = 'S'
while R == 'S':
    contador += 1
    num = int(input('Digite um número: '))
    soma += num
    if maior < num or contador == 1:
        maior = num
    if menor > num or contador == 1:
        menor = num
    R = input('Gostaria de continuar? S/N ').upper().strip()
print(f'Média: {soma/contador:.2f}. Maior número = {maior}. '
      f'Menor número = {menor}')
