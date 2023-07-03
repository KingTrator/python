m = float(input('Digite um número inteiro: '))
n = m/2
if n == int(m/2):
    print('Este número é par.')
else:
    n == float(m/2) # Está parte é desnecessária, bastaria deixar o print.
    print('Este número é ímpar.')

# Estou feliz, porque este código é funcional, embora não siga a recomendação
# padrão de vericicação de paridade em Python, que costuma usar %.
# Abaixo, a forma padrão de executar a verificação de paridade.
num = int(input('Digite um número inteiro: '))

if num % 2 == 0: # Se o resto da divisão por 2 for igual a zero:
    print('Este número é par.')
else: #Se o resto não for 0, só pode ser ímpar. Este código aqui é mais direto.
    print('Este número é ímpar.')
