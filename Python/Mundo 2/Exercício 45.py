import random
# Fico feliz com este código, pois ele é mais simples e eficiente que o código do
# Gunabara :)
print('Olá! Vamos jogar jokenpô?')
rola = str(input('O que você decidiu jogar? '))
jogador = rola.lower()
computador = random.choice(['pedra', 'papel', 'tesoura'])
if jogador == computador:
    print('Empatamos! Também joguei {}'.format(jogador))
elif (computador == 'pedra' and jogador == 'tesoura') or (computador == 'papel' and jogador == 'pedra')\
     or (computador == 'tesoura' and jogador == 'papel'):
    print('Ganhei! Joguei {}'.format(computador))
else:
    print('Perdi :/ \nBem, parabéns para você! Joguei {}'.format(computador))
