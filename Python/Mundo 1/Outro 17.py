import math
alfa = float(input('Digite o valor de um ângulo qualquer'))
conversao = math.radians(alfa)
sa = math.sin(conversao)
ca = math.cos(conversao)
ta = math.tan(conversao)
print('Para o valor fornecido, o seno é {}, o cosseno é {} e a tangente é {}'.format(sa, ca, ta))
# Devido a maneira com a qual os computadores processam informações numéricas,
# este script não está perfeito. Por exemplo, o script não é capaz de retornar
# cos(90º) = 0, mas em vez disso ele retonar um valor muito pequeno, que, para fins
# práticos, é zero.
# A seguir, desenvolvo uma correção ancorada no chatGPT-4.
beta = float(input('Digite o valor de um ângulo qualquer '))
cv = math.radians(beta)
saa = math.sin(cv)
caa = math.cos(cv)
taa = math.tan(cv)
if abs(saa) < 1e-10:
    caa = 0
if abs(saa) < 1e-10:
    saa = 0
if abs(taa) > 1e10:
    taa = print('A tangente tende ao infinito')

print('Para o valor {},\n O seno é {} \n O cosseno é {} \n A tangente é {}'.format(beta, saa, caa, taa))

#A solução não está funcionando.