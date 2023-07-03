# Para uma entrada N do usuário, mostre os N primeiro números da
# Sequência de Fibonacci (0, 1, 1, 2, 3, 5, 8, 13, 21, 34, 55, 89, 144...)
N = int(input('Digite um número \033[1mINTEIRO: \033[m'))
a = 0
b = 1
S = 'S'
m = 0
if N >= 1:
    print(a)
if N >= 2:
    print(b)
c = 2
S = 'S'
while S == 'S':
    while c < N + m:
        fib = a + b
        print(fib)
        a = b
        b = fib
        c += 1
    S = input('Gostaria de continuar vendo a sequência? S/N ').upper().strip()
    if S == 'S':
        m = int(input('Digite um número \033[1mINTEIRO: \033[m'))
print('Acabou')
