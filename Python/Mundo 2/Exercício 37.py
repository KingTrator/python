from time import sleep

print('Olá! Seja bem vindo ao conversor de sistemas decimais.')
n = int(input('Para converter um número inteiro para binário, digite 1.'
               '\nPara converter um número inteiro para octal, digite 2.\n'
               'Para converter um número inteiro para hexadecimal, \ndigite 3: '))
if n == 1:
    b1 = int(input('Certo! Digite o inteiro que deseja converter para binário: '))
    b11 = bin(b1)
    print('Processando...')
    sleep(3)
    print(b11)
elif n == 2:
    b2 = int(input('Certo! Digite o inteiro que deseja converter para octal: '))
    b22 = oct(b2)
    print('Processando...')
    sleep(3)
    print(b22)
elif n == 3:
    b3 = int(input('Certo! Digite o inteiro que deseja converter '
                   'para hexadecimal: '))
    b33 = hex(b3)
    print('Processando...')
    sleep(3)
    print(b33)
else:
    print('Reinicie o programa e digite somente 1, 2 ou 3.')

