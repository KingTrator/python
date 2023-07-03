s = 0
print('Caso queira parar, digite 999')
while True:  # Looping infinito
    n = int(input('Digite um número inteiro: '))
    if n == 999:
        break
    s += n
print(f'A soma dos números digitados é {s}.')
