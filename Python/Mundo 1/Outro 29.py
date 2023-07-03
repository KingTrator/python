from pygame import mixer
from time import sleep
from random import randint

print('Olá, vamos jogar um jogo?')
print('Eu vou pensar em um número de 0 a 5...')
sleep(1)
print('E você deve tentar advinhá-lo. Mas apenas números inteiros, ok? Então vamos lá!')
sleep(1)
jogador = int(input('Em qual número eu pensei? '))
n = randint(0, 5)

print('Processando...')
print('===='*20)
sleep (5)

if jogador == n:
    print('Uau! Você acertou!')
elif jogador > 5 or jogador < 0:
    print('Você não consegue nem seguir dicas simples, não é? Eu disse que pensaria em um número'
          '\nde 0 a 5. {} não está no intervalo.'.format(jogador))
else:
    print('Eu pensei em {}! Hahahaha, eu ganhei!'.format(n))
    mixer.init()
    mixer.music.load('C:/Users/Win10/OneDrive/Desktop/chaves-ta-bom-mas-nao-se-irrite.mp3')
    mixer.music.play()
    while mixer.music.get_busy():  # espera até a música acabar
        sleep(1)
