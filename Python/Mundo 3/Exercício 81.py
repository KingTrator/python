c = c5 = 0
num = []
while True:
    n = int(input('Digite um número: '))
    if n == 5:
        c5 += 1
    num.append(n)
    c += 1
    pergunta = input('Gostaria de sair? ').strip().upper()
    if pergunta == 'S':
        break
num.sort(reverse=True)
if c5 != 0:
    print(f'O número cinco está na lista {num}')
    print(f'Foram digitados {c} números')
else:
    print(f'O número cinco não está na lista {num}')
    print(f'Foram digitados {c} números.')
# Posso ser um pouco mais rápido, fazendo o append direto na lista,
# sem criar uma linha a mais. Observe abaixo:
numeros = []
while True:
    numeros.append(int(input('Digite um número: ')))
    question = input('Gostaria de sair? S/N ').strip().upper()
    if question == 'S':
        break
numeros.sort(reverse=True)
if 5 in numeros:
    print(f'O número cinco está na lista {numeros}')
    print(f'Foram digitados {len(numeros)} números')
else:
    print(f'O número cinco não está na lista {numeros}')
    print(f'Foram digitados {len(numeros)} números.')
