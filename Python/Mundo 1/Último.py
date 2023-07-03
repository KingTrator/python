#from random import randint
#n = randint(1, 36)
#if n != 1 and n != 2 and n != 3 and 1 != 14 and n != 15 and n != 16 and \
#        n != 17 and n != 25 and n !=26 and n != 24:
#    print(n)

#n = randint(1, 36)
#if n not in [1, 2, 3, 14, 16, 16, 17, 24, 25, 26]:
#   print(n)
#else:
#    print('Try again, bitch.')


print('\033[0;30;41mTexto colorido\033[m')
# Texto e fundo de iguais cores
print('\033[1;33;43mOlá Mundo!\033[m')
print('\033[1;36;40mOlá mundo!\033[m')
print('\033[1;36;40mOras, agora posso descrever a história de minha vida com muita'
      ' qualidade!\033[m')
# name = input('\033[1;36;40mDigite seu nome completo: \033[m').strip()
# v = name.split()
# v1 = name.upper()
# v2 = v1.find('SILVA')
#
# if v2 == True:
#     print('\033[1;36;40mSeu nome possui Silva. \033[m')
# else:
#     print('\033[1;36;40mBelo nome!\033[m')
#Note que \033[m fecha as cores. Isso é útil nestes casos:
nome = 'Pica'
print('Olá! Muito prazer em te conhecer {}{}{}.'.format('\033[0:33:40m', nome, '\033[0:33:40m'))
# No entanto, posso evitar o que acontece:
print('Olá! Muito prazer em te conhecer {}{}{}.\033[m'.format('\033[0:33:40m', nome, '\033[0:33:40m'))
# Inclusive:
print('Olá! Muito prazer em te conhecer \033[m{}{}{}.\033[m'.format('\033[0:33:40m', nome, '\033[0:33:40m'))
# Por fim
print('Olá! Muito prazer em te conhecer \033[0:33:40m{}.\033[m'.format(nome))
# Outra possibilidade é a criação de um dicionário de cores, o que, sem dúvidas,
# facilita a vida
print('\n \n')
name = input('Qual o seu nome filhão? ')
cores = {'HR':'\033[1;31m', 'WB':'\033[7;30;47m', 'Blue':'\033[1;34m'}
print('{}{}\033[m? Gosto muito de {}{}\033[m. Bem, seja bem vindo {}{}!\033[m!'.format(cores['HR'],  name,
    cores['Blue'], name, cores['WB'], name))





