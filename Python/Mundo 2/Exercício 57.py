s = ''
while s != 'M' and s != 'F':  # usar "or" quebra o código. While equivale a um if, mas faz looping.
    s = input('Qual o seu sexo? (M/F) ').upper()
    if s != 'M' and s != 'F':  # igual aqui, "or" quebra tudo.
        print('Por favor, digite apenas M ou F.')
print('OBRIGADO!')
