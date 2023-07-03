# O código abaixo está sim funcional, mas é possível simlificá-lo
# e torná-lo menos propenso a erros, com a diminuição do número de loopings internos.
'''a1 = float(input('Digite o primeiro termo da PA: '))
r = float(input('Digite a razão da PA: '))
q = 0
c = 0
d = 0
while q != 10:
    q += 1
    print(a1, end='|')
    a1 += r
    if q == 10:
        b = input('Você gostaria de ver mais termos? S/N ').upper()
        if b == 'S':
            n = int(input('Quantos números a mais você gostaria de ver? '))
            if n > 1000:
                print('Por favor, não exagere!')
                break
            else:
                while c != n and n > 0:
                    print(a1, end='|')
                    c += 1  # Contador para a parada do looping interno
                    d += 1   # Contador que analisa se há números demais em uma linha, se sim, pula linha.
                    a1 += r
                    if 50 < d < 1000:
                        print('\n', a1)  # Repete o último a1 da linha anterior na nova.
                        d = 0
        elif b == 'N':
            print('Ok! O programa está encerrado.')
print('\n')
print('Programa encerrado.')'''
n = float(input('Digite o primeiro termo da PA: '))
r = float(input('Digite a razão da PA: '))
termos = 10  # Inicialmente, mostra-se apenas alguns termos da PA.
d = 0  # Verificação para pular linhas a cada 50 termos.
c = 0  # Verificação do número de termos a serem analisados.
while c < termos:
    c += 1
    d += 1
    if d < 50:
        print(n, end='|')
        n += r
    if d == 50:
        d = 0
        print(n)
        n += r
    if c == termos:
        print('\n')
        m = int(input('Quantos termos a mais você gostaria de ver? '))
        termos = m
        c = 0
        if m > 1000:
            print('Por favor, não exagere!')
            break
print('Programa encerrado.')
