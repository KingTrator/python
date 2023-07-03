d = int(input('Digite o número em Km, e apenas o número, da distância a ser percorrida'
                  ' na sua viagem: '))
p1 = d * 0.5
p2 = d * 0.45 # desnecessário.
if d < 200:
    print('O preço total é R${}.'.format(p1))
else:
    print('O preço total é R${}.'.format(p2))
# Outra maneira de resolver o problema é usando o if em uma única linha,
# mas isso é um caso bem específico e não é recomendado pelo Guanabara.

# p = d * 0.5 if d < 200 else p = d * 0.45
# print('O preço da passagem será de R${}.'.format(p))
# Note que sequer é preciso criar p1 e p2, pois o valor de p está dentro das condicionais

# Refazendo o primeiro código
print('\n')
dd = int(input('Digite a distância da sua viagem: '))
if dd < 200:
    p = dd * 0.5
    print('O preço é {}'.format(p))
else:
    p = dd * 0.45
    print('O preço é {}'.format(p))
# Assim o código fica mais curto e elegante.