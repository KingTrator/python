# Outras funções de manipulação de texto. Parecem úteis para cálculos de
# combinatória.
frase = 'O rato roeu a roupa do rei de Roma'
M = frase.split()
K = '|'.join(M)
print(K)
print(M)
print(frase.find('roeu'))
# O print, neste caso, de frase.find('roeu') irá dar a localização da palavra
# com base na primeira letra que aparece 'r', a qual está, sem realizar um split,
# na posição 7 dos caracteres. Para deixar mais preciso, seria necessário uma
# correção. O chatGPT sugeriu a que se segue.
indice_roeu = M.index('roeu')
print(indice_roeu)
print('\n')
print('Caso queira colocar em print uma frase muito longa, use aspas triplas. \n')
print('''ele foi ali na esquina
eu fiquei à deriva
ela foi tomar um chopp
eu fiquei na janela
meu amor
foi ao cinema
eu aqui virando as cartas
ele foi até a praça
ela foi brincar com fogo
eu fiquei ali na rua
meu amor
não disse onde
ela foi regar as ondas
eu fiquei aqui na fila
foi pegar um touro a unha
eu fiquei regando frases''')