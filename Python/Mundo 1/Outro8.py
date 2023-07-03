X = int(input('Digite um número inteiro: '))
Y = X - 1
Z = X + 1
print('Você digitou {}, que é antecedido por {} e sucedido por {}'.format(X, Y, Z))

# Este código está funcional.

P = int(input('Digite um número inteiro: '))
R = P ** 0.5
L = P * 2
print('Você digitou {}, cuja raiz quadrada, considerando-se até 3 cases decimais, é {:.3f} e cujo dobro é {}'.format(P, R, L))

# O código está funcional.
print('\n \n')

v = int(input('Digite um número inteiro para descobrir sua tabuada: '))
v1 = v * 1
v2 = v * 2
v3 = v * 3
v4 = v * 4
v5 = v * 5
v6 = v * 6
v7 = v * 7
v8 = v * 8
v9 = v * 9
print('A tabuada do 1 ao 9 de {} é, na ordem, {}, {}, {}, {}, {}, {}, {}, {}, {}, '.format(v, v1, v2, v3, v4, v5, v6, v7, v8, v9))
# O código está funcional.
# Existe uma outra maneira de exibir esta tabuada, a qual também é bem interessante.
# Abaixo, está ela.
print('\n \n ')
num = int(input('Digite um número inteiro para ver sua tabuada: '))
print('({} x {} = {}),'.format(num, 1, num*1), end=' ')
print('({} x {} = {}),'.format(num, 2, num*2), end=' ')
print('({} x {} = {}),'.format(num, 3, num*3), end=' ')
print('({} x {} = {}),'.format(num, 4, num*4), end=' ')
print('({} x {} = {}),'.format(num,5, num*5))
print('({} x {} = {}),'.format(num, 6, num*6), end=' ')
print('({} x {} = {}),'.format(num, 7, num*7), end=' ')
print('({} x {} = {}),'.format(num, 8, num*8), end=' ')
print('({} x {} = {}).'.format(num, 9, num*9))
# Essa maneira me parece mais elegante. (Na verdade, não é não. O end deu uma
# bagunçada no código e eu precisaria pensar para ajustá-lo. No entanto,
# o chatGPT me ofereceu um código MUITO MAIS ELEGANTE e simples para utilizar.
# Segue o código abaixo
numl = int(input('Digite um número inteiro para ver sua tabuada: '))
for i in range(1, 10):
    print('{} x {} = {}'.format(numl, i, numl*i))




RS = float(input('Diga-me quantos reais você tem e eu lhe direi quantos dólares poderá comprar'
                       ' com base na cotação atual'))
# Não se usa vírgula para casas decimais no Python, isto é, 4,99 leva a outra resposta em relação
# a 4.99
SD = RS / 4.99
print('Pelos dados fornecidos, digo-lhe que com {} você pode comprar {} dólares'.format(RS, SD))

#O código está funcional.



