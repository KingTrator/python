print('Este script diz qual o tipo do triângulo e se é possível ou não o formar.')
x = float(input('Lado: '))
y = float(input('Lado: '))
z = float(input('Lado> '))
if (x + y > z) and (x + z > y) and (y + z > x):
    print('É possível formar um triângulo.')
    if x == z == y:
        print('O triângulo é equilátero')
    elif (x == z) or (x == y) or (z == y):
        print('O triângulo é isósceles')
    else:
        print('O triângulo é escaleno')
else:
    print('{} Não {} é possível formar um triângulo.'.format('\033[1m', '\033[m'))
