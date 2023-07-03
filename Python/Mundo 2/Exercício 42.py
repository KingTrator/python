print('Este script calcula o IMC.')
peso = float(input('Digite o peso em kg: '))
altura = float(input('Digite a altura em metros: '))
IMC = peso/(altura**2)
if IMC < 18.5:
    print('{:.2f} é abaixo do peso'.format(IMC))
    print('Critério: abaixo de 18.5.')
    novo_peso = 18.5 * (altura **2)
    print('Seu peso ideal é {:.2f}.'.format(novo_peso))
elif 25 > IMC >= 18.5:
    print('{:.2f} é o peso ideal'.format(IMC))
    print('Critério: maior ou igual a 18.5, mas abaixo de 25.')
elif 30 > IMC >= 25:
    print('{:.2f} é sobrepeso'.format(IMC))
    print('Critério: maior ou igual a 25 e menor que 30.')
    novo_peso = 25 * (altura ** 2)
    print('Seu peso ideal é {:.2f}'.format(novo_peso))
elif 40 > IMC >= 30:
    print('{:.2f} é obesidade'.format(IMC))
    print('Critério: maior ou igual a 30, mas abaixo de 40.')
    novo_peso = 25 * (altura ** 2)
    print('Seu peso ideal é {:.2f}'.format(novo_peso))
else:
    print('{:.2f} é obesidade mórbida.'.format(IMC))
    print('Critério: acima de 40.')
    novo_peso = 25 * (altura**2)
    print('Seu peso ideal é {:.2f}'.format(novo_peso))
