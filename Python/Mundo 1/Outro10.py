# Custo: 60 reais diário + 0,15 real por Km rodado.
D = int(input('Por quantos dias o carro foi alugado?'))
K = round((float(input('Quantos Km o carro percorreu?'))))
P = (D*60) + (K*0.15)
print('Considerando-se o tempo de aluguel em dias, {}, mais a quantidade de Km rodados,'
      '{}, o custo total do aluguel é de R${}'.format(D, K, P))

# A função round irá arredondar o valor encontrado pela função float.
# Observe que todo input retorna uma string. O float converte a string para um
# valor flutuante. Como a função round só aceita valores int ou float, isso é neces
# sário. Então com a conversão em float, podemos usar um valor arredondado pela
# função round.
# Os critérios de arredondamento são: _.5 é arredondado para o par mais próximo.
# Se o valor for _.n em que n é imediatamente menor que 5, então se arredonda para baixo.
# Se n for maior que 5, arredonda-se para cima.

# O problema desse script é que ele não considera que 8.1 dia deve ser dado como
# 9 dias para uma empresa, por exemplo.
# Há como consertar isso por meio da biblioteca mathplotlib, mas não é necessário
# neste exemplo mais trivial