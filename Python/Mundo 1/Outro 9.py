# Talvez eu devesse criar uma pasta especial para desafios, são tantos, que me falta
# espaço para escrevê-los de modo a não tornar as pastas muito cheias.

#Largura e altura da parede
print('Bem vindo! Use este script para calcular a área de uma parede e definir quanta'
      '\n tinta, em litros, será necessária para pintá-la.')
L = float(input('Expresse a largura, apenas números em metro (m)'))
H = float(input('Expresse a altura, apenas números em metro (m)'))
A = L * H
V = A / 2
print('Para pintar {}m² de parede, será necessário {} litros de tinta'.format(A, V))
print('OBSERVAÇÃO: considere que 1L de tinta pinta 2m² de parede')
# O código está funcional. 09/05/2023
# A seguir, o print é usado para gerar um espaço entre os dois códigos, isto é
# gerar línhas em branco.
print('\n \n \n \n \n \n')
print('O script a seguir serve para calcular 5% de desconto sobre um produto qualquer')
D = float(input('Por favor, diga o valor do produto'))
Dmenor = D * 0.95
print('O produto passará a custar {:.2f} com 5% de desconto'.format(Dmenor))
# O script está funcional. 09/05/2023
print('\n \n \n \n \n \n')
S = float(input('Qual o valor do salário do funcionário em reais?'))
Ss = S * 1.15
print('O novo salário, com aumento de 15%, será de {:.2f} reais.'.format(Ss))
# O código está funcional. 09/05/2023
print('\n \n \n \n \n \n')
Tf = float(input('Digite a temperatura em Fahrenheit '))
Tc = (Tf - 32) / 1.8
print('{} em graus Celsius é {}'.format(Tf, Tc))
#O código está funcional. 09/05/2023


