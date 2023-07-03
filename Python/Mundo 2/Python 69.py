condicao = True
ci18 = cs = csi20 = 0
while condicao:
    i = int(input('Qual a sua idade? '))
    if i > 18:
        ci18 += 1
    s = input('Qual o seu sexo? M/F ').upper().strip()
    if s != 'M' and s != 'F':
        print('Erro. Digite apenas M ou F.')
    if s == 'M':
        cs += 1
    if s == 'F' and i < 20:
        csi20 += 1
    condicao = input('Você quer continuar a cadastrar pessoas? S/N ').strip().upper()
    if condicao == 'N':
        condicao = False
print(f'{ci18} pessoas são maiores de idade. {cs} são homens. '
      f'{csi20} são mulheres com menos de 20 anos,')
