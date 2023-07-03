'''from math import factorial
print('Olá! Bem vindo à cálculadora de fatoriais')
print('A seguir, digite um fatorial qualquer, e veja quanto ele vale.')
n = int(input('Digite um número: '))
print(factorial(n))'''
# Só para deixar claro, há uma função específica para isso, usar while e
# for é só para resolver o exercício como o proposto.
print('Olá! Bem vindo à calculadora de fatoriais')
print('A seguir, digite um fatorial qualquer, e veja quanto ele vale.')
n = int(input('Digite um número: '))
c = 1
b = 0
while n > 1:
    if n > 300:
        print('Números tão altos podem quebrar o programa. Por favor, reinicie-o.')
        break
    b = (n * (n - 1)) * c
    c = b
    n = n - 2
if n >= 0:
    print(c)
else:
    print('Os fatoriais devem ser números maiores ou igual a 0. Escolha um número válido.')

# Resolvendo o exercício com for
m = int(input('Digite um número: '))
if m > 0:
    for i in range(1, m):  # O m já é o 5. Então a primeira multiplicação será 5 * 1.
        if n > 300:
            print('Números tão altos irão quebrar o programa. Por favor, reinicie-o.')
            break
        m *= i

    if m == 0:
        print(1)
    else:
        print(m)

jota = int(input('Digite um número: '))
cara = 1
if jota > 0:
    print('5! --> ', end=' ')
    while jota > 0:
        print(f'{jota} x ' if jota > 1 else f'{jota} = ', end='')
        bota = jota
        jota -= 1
        cara = bota * cara
    print(f'{cara}')





