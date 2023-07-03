n = float(input('Digite o primeiro termo da PA: '))
r = float(input('Digite a razão da PA: '))
q = 0
x = 0
while q < 10:
    if q == 0:
        print(f'{n:.2f}', end=' ')  # No caso, como é uma PA, para que de fato ela
        x += (n + r)
    else:
        print(f'{x:.2f}', end=' ')  # seja coerente, seria bom nem usar ":.2f".
        x += r
    q += 1
m = float(input('Digite o primeiro termo da PA: '))
k = float(input('Digite a razão da PA: '))
y = 0
print(m)
while y < 9:
    m += k
    print(m)
    y += 1
print('ACABOU')
