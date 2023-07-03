from random import randint
# Aprimoramento do exercício 28
f = 0
t = 0
print('Bem vindo ao jogo da advinhação! Digite um número de 1 a 10, se acertar o número que pensei,'
      ' você ganha!')
n = int(input('Digite o número: '))
n2 = randint(1, 10)
if n == n2:
    print('Parabéns!! Você acertou de primeira!')
else:
    print(f'Você errou. Eu pensei em {n2}.')
    f += 1
    while t == 0:
        n2 = randint(1, 10)
        n = int(input('Tente de novo: '))
        print(f'Eu pensei em {n2}')
        if n == n2:
            t += 1  # O código ficaria mais curto se eu trocasse isso por break.
        else:
            f += 1
    print(f'Parabéns! Você acertou! Foram necessárias {f} tentativas.')
