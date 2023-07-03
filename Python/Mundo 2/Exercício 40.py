n1 = float(input('Digite a 1ª nota: '))
n2 = float(input('Digite a 2ª nota: '))
m = (n1 + n2)/2
if m >= 6.9:
    print('Aprovado.')
elif 5.0 < m < 6.9:
    print('Recuperação')
else:
    print('Reprovado')
