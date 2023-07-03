from time import sleep
print('Olá! Bem vindo à sua calculadora em Python de até 2 casas decimais!')
print('Digite dois números quaisquer e selecione a operação que deseja'
      'efetivar:'
      '\n [1] Soma'
      '\n [2] Multiplicação'
      '\n [3] Verificar qual deles é o maior'
      '\n [4] Inserir novos números'
      '\n [5] Terminar o programa')
n1 = float(input('Qual o primeiro valor? '))
n2 = float(input('Qual o segundo valor? '))
c = 0
n = 0
V = ''  # Permite que o usuário relembre os comandos.
while n != 5:
    if c == 10:
        c = 0
        V = input('Gostaria de relembrar os comandos? S/N ').upper()
        if V == 'S':
            print('Relembrando:'
                  '\n [1] Soma'
                  '\n [2] Multiplicação'
                  '\n [3] Verificar qual deles é o maior'
                  '\n [4] Inserir novos números'
                  '\n [5] Terminar o programa')
    n = int(input('Por favor, selecione uma das opções.'))
    c += 1
    if n == 1:
        print(f'A soma deles é {(n1 + n2):.2f}')
    elif n == 2:
        print(f'O produto entre eles é {(n1 * n2):.2f} ')
    elif n == 3:
        maior = max(n1, n2)
        print(f'O maior deles é {maior}.')
    elif n == 4:
        print('Claro! Escolha novos números!')
        n1 = float(input('Qual o primeiro valor? '))
        n2 = float(input('Qual o segundo valor? '))
    elif n == 5:
        print('Certo, encerrando o programa...')
        sleep(1)
    else:
        print('Por favor, escolha uma opção válida.')
        c = 10
print('Programa encerrado.')
# Eu preciso parar de "rushar" fiz o código do começo ao fim sem nem
# o testar antes de terminá-lo...
# Porém, não errei! HAHAHAHA (mas isso não pode me condicionar ao mau hábito)
