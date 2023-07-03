s = float(input('Informe o seu salário atual: R$ '))
if s >= 1250:
    print('Seu aumento será de 10%')
    print('Novo salário: {:.2f}'.format(s * 1.1))
else:
    print('Seu aumento será de 15%')
    print('Novo salário: {:.2f}'.format(s * 1.15))
# o código está funcional.