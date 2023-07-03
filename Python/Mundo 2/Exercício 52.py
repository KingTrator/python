print('\033[33m bem vindo ao\033m \033[1;33m IDENTIFICADOR DE PRIMOS\033[m')
p = int(input('Digite um \033[1mINTEIRO\033[m para verificar se é ou não primo: '))
d = 0
if p <= 1:
    print('{} não é primo.'.format(p))
else:
    for i in range(2, int(p**0.5) + 1):  # o GPT-4 diz que o laço (2, int(p**0.5) + 1) é mais eficiente.
        if p % i == 0:
            d = d + 1
            break
if d >= 1:
    print('{} não é primo'.format(p))
elif d == 0 and p >= 2:
    print('{} é primo.'.format(p))
# O Kaiky me enviou a prova de que o laço (2, int(p**0.5) + 1) é
# um método mais eficiente de calcular números primos. Abaixo, a prova disso.
# Suponha a, b e c números inteiros maiores que 1.
# Se a = bc, então sqrt a > b ou sqrt a > c.
# Isso porque: sqrt a . sqrt a = a
# Se c = sqrt a, então b = sqrt a.
# Se c > sqrt a, então b < sqrt a. E vice-versa.
# Portanto, um número a que pode ser escrito como bc, segue sqrt a > b ou
# sqrt a > c, porque se ocorrer b != c, então um deles deve ser maior e o outro
# menor que a sqrta.
# Como procuramos por um número inteiro A qualquer que seja primo, basta procurarmos
# somente até a parte inteira de sqrt A, pois se A não for primo,
# então haverá ao menos dois números que podem ser multiplicados para alcançar
# ele. Se A for primo, sua raiz não será exata. O código pega apenas
# a parte inteira e divide o primo. Naturalmente, a divisão não será exata
# pois o valor usado é um inteiro e não a raiz do primo.
# Se o número não for primo, ao ser dividido por algum de seus antecessores
# mas não necessariamente por sua raiz inteira, ao menos uma das respostas
# dará resto == 0. É bem legal.