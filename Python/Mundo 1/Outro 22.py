frase = 'Curso em Vídeo'
print(frase[6:10])
print('A palavra Curso está escrita na frase?','Curso' in frase)
print('A palavra Pica está escrita na frase?', 'Pica' in frase)
print('Aumentando a letra da frase "Curso em vídeo", {}.'.format(frase.upper()))
print('Reduzindo a letra {}.'.format(frase.lower()))
print('\n')
print('Suponha que alguém precisa digitar o próprio nome em uma caixa de texto...\n'
      '... no entanto, essa pessoa adiciona espaços indevidos que poderão resultar\n'
      'em erro de leitura.')
print('\n ')
nome = '      John AFK     '
print(nome)
print('Correção do nome: {}'.format(nome.strip()))
print('Se, por alguma razão, for necessário remover apenas o espaço da direta...')
nm = '     JOHNNY AFUK      '
print('Correção do nome: {}, correto?'.format(nm.strip()))
print('Correção do nome: {}, correto?'.format(nm.rstrip()))



