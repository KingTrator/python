print('Olá! Bem vindo à tabuada em Python.')
p = 0
while True:
    print('\n')
    n = int(input('Digite um número inteiro positivo para ver sua tabuada: '))
    print('Se quiser encerrar o código, digite um número negativo como -1.')
    if n < 0:
        break
    for i in range(1, 11):
        p = n * i
        print(f'{n} x {i} = {p}')
print('ACABOU')
