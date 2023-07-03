import math
from time import sleep
print('\033[1mO programa a seguir serve para calcular o lado de '
      'um triângulo retângulo.\033[m')
sleep(2)
X = float(input('\033[1mDigite o valor de um dos catetos:\033[m '))
Y = float(input('\033[1mDigite o valor do outro cateto:\033[m '))
angle = float(input('\033[1mDigite o ângulo entre os catetos '
                    '(apenas o número, sem símbolos)\033[m'))
angle = math.radians(angle)
H = (((X ** 2) + (Y ** 2)) - (2*X *Y*math.cos(angle)))
print('{}'.format('\033[4;45m'), '='*120, '{}'.format('\033[m'))
print('{} O terceiro lado do trângulo é {}.{}'.format('\033[1m', math.sqrt(H), '\033[m'))
print('{} O valor do ângulo, em radianos, é de:'.format('\033[1;36m'), angle)

# Tome esta nota do chatGPT-4:
#A função math.radians() converte um ângulo de graus para radianos.
# Radianos são uma unidade de medida para ângulos usada principalmente em matemática e física, e são baseadas no raio de um círculo.

# Um círculo completo é igual a 2π radianos, o que equivale a 360 graus.
# Portanto, um ângulo de 180 graus seria igual a π radianos, que é aproximadamente 3.14159. Um ângulo de 90 graus seria igual a π/2 radianos, que é aproximadamente 1.5708.

#Então, quando você imprime angle_rad após converter o ângulo de graus
# para radianos, o valor que você vê é o ângulo em radianos, não em graus. Se esse valor for maior que 1, isso simplesmente significa que o ângulo em graus é maior que 180/pi, ou cerca de 57,3 graus.

#Naturalmente, este código tem um problema: ele não verifica se, para começar, os dados
# que o usuário fornece de fato são reais, isto é, se de fato existe um triângulo
# com aquelas características.
# Por exemplo, o usuário deveria receber uma mensagem de erro se ao digitar 4 e 4
# e ângulo = 45º, afinal, neste caso, o ângulo interno do triângulo seria maior
# que 180º, o que é impossível.
