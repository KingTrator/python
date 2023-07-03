from time import sleep
#Agora vamos aprender algumas funções para identificar se o input é
#numérico ou alfabético.
n = input('{}Digite algo:{} '.format('\033[1;4m', '\033[m'))
print('{}Verificando se {} é numérico...{}'.format('\033[1;4m', n, '\033[m'))
print('\n')
sleep(2)
print('\033[1;32m', n.isnumeric(),'\033[m')
#Se você digitar apenas números, isnumeric dará como resposta True (is numeric)
# Se você digitar um número + letra ou apenas letras, dará False (is not numeric)
#Há inúmeras funções do tipo "is" disponíveis. Ao digitar "is" dentro de algum
# input, por exemplo, o app já deve trazer inúmeras sugestões, que vc intui
# a função pelo nome, ou pede para que o chatGPT te diga.
#Vamos ficar por aqui, por ora. É mais a critério de curiosidade.
#Até então, não vejo muita utilidade do Python para mim na intenção de criar
#jogos, mas tenho me divertido.

# APÓS TERMINAR O EXERCÍCIO ORIGINAL, RETORNEI, AO FINAL DO MUNDO 1 DE PYTHON
# PARA IMPLEMENTAR MEU CÓDIGO COM CORES E COM A IMPORTAÇÃO DE UMA FUNÇÃO.