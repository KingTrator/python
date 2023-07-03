import math
'''print('Por favor, digite as retas no padrão ax + b.')
r1 = str(input('Digite a reta r1: ')).strip()
r2 = str(input('Digite a reta r2: ')).strip()
r3 = str(input('Digite a reta r3: ')).strip()
r1.replace('', ' ')
r2.replace('', ' ')
r3.replace('', ' ')
a = r1.split()
b = r2.split()
c = r3.split()
a1 = float(a[0])
b1 = float(b[0])
c1 = float(c[0])
matriz = (-a1) + (-b1) + (-c1)'''
# Vamos tentar de novo:
# Entendi o que aconteceu. O Guanabara se expressou mal. Eu estava realizando
# um exercício para tentar verificar se três retas quaisquer poderiam formar
# um triângulo. Desde que o "a" delas seja distinto dois a dois, então elas podem formar.
# Mas acho que a intenção era saber se "segmentos de reta", dadas as condições de existência
# do triângulo, podem ou não formar um triângulo. De todo modo, vou realizar as duas
# possibilidades de exercício.
print('Digite três retas, a seguir, e lhe direi se elas podem ou não formar um triângulo')
print('Observação: o formato deve ser ax + b. Além disso, dê um valor para a, ao contrário, o programa resultará em '
      ' erro.')
r1 = str(input('Reta 1ª: ')).strip()
r2 = str(input('Reta 2ª: ')).strip()
r3 = str(input('Reta 3ª: ')).strip()
a = r1.replace('', ' ')
b = r2.replace('', ' ')
c = r3.replace('', ' ')

a1 = a.split()
b1 = b.split()
c1 = c.split()

a2 = float(a1[0])
b2 = float(b1[0])
c2 = float(c1[0])

if a2 == b2 == c2:
    print('As retas não poderão formar um triângulo, pois são paralelas.')
else:
    print('As retas poderão formar um triângulo.')

# Outra interpretação do exercício é a de atender as condições de existência do
# triângulo.
G1 = float(input('Digite o tamanho do lado l1'))
G2 = float(input('Digite o tamanho do lado l2'))
G3 = float(input('Digite o tamanho do lado l2'))
if G1 + G2 > G3 and G3 + G2 > G1 and G1 + G3 > G2:
    print('Essas medidas permitem formar um triângulo.')
else:
    print('As condições de existência do triângulo não foram respeitadas, portanto,'
          '\nnão é possível formar um triângulo com essas três medidas.')
# Os dois códigos estão funcionando.



