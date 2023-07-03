from time import sleep
print('Olá! Se você deseja um empréstimo para comprar um imóvel'
      '\npor favor, responda às seguintes perguntas.')
sleep(2)
VC = float(input('Qual o valor da casa que você deseja comprar? R$'))
S = float(input('Qual o valor do seu salário líquido? R$'))
T = int(input('Em quantos anos você pretende quitar o valor da casa? '))
E = VC / (T*12)
if E <= (1.3 * S):
    print('Processando...')
    sleep(5)
    print('Muito bem! Seu empréstimo de R${:.2f} foi \033[1maprovado!\033[m'.format(E))
else:
    print('Processando...')
    sleep(5)
    print('Lamento, mas o seu empréstimo \033[1mnão foi aprovado\033[m.')
    print('Por favor, busque entrar em contato com o seu gerente para')
    print('entender melhor a situação.')
