# Vamos trabalhar com algumas das funcionalidades da biblioteca math
#Note que ao importar a biblioteca, VOCÊ DEVERÁ usar o prefixo math.FUNÇÃO
# Ou seja, não basta escrever sqrt(x), mas sim math.sqrt(x) para x = qualquer valor.
import math
n = float((input('Digite algo')))
n2 = math.sqrt(n)
n3 = n/7
print('Para {}, temos que a raiz quadrada é {}, a divisão \n por 7 é, em até duas casas decimais, {:.2f}, que se aproxima'
      'de {} para cima e de {} para baixo.'.format(n, n2, n3, math.ceil(n3), math.floor(n3)))
# O programa está funcional e operante.
# Caso quisesse utilizar apenas da função ceil, floor e sqrt, poderia ter feito:
# from math import ceil, floor, sqrt