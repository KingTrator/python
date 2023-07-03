# O programa deve ler várias entradas em int do usuário. OK.
# O programa deverá salvar valores únicos das entradas, isto é, não mostre duplicatas. OK.
# O programa deverá mostrar os valores digitados em ordem crescente. OK.
l = []
while True:
    n = int(input('Digite um número inteiro: '))
    if n not in l:
        l.append(n)
    else:
        print('Valor duplicado, não será adicionado.')
    resp = input('Gostaria de sair? S/N ').upper().strip()
    if resp == 'S':
        break
print(f'Os números (únicos) digitados foram: {sorted(l)}')

# Verifique com o GPT-4 porque o código abaixo não funciona como se propõe:
'''l = []
q = 0
while True:
    n = [int(input('Digite um número inteiro: '))]
    l = n + l
    resp = input('Gostaria de sair? S/N ').upper().strip()
    if resp == 'S':
        break
    q += 1
print(f'Os números (únicos) digitados foram: {l}')'''
# Cheguei a considerar que o problema fosse o estabelecimento de uma ligação entre n e l
# por conta do sinal de recebe "=", mas na verdade o que ocorre é que, para o Python,
# toda vida que o looping ocorre, "n" é uma nova lista ainda que o valor seja igual ao único valor
# de "l". É uma peculiaridade da linguagem. Como distinguri um clone de bactéria A por A', o Python
# diferente igualdade de identidade.
