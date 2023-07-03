from random import randint
a = ()
maior_valor = menor_valor = 0
for i in range(5):
    b = (randint(1, 5))  # Usar , tornou isso uma tupla. Thank you GPT-4. (Nem o chamei, ele me disse isso antes do problema).
    if b > maior_valor or i == 0:
        maior_valor = b
    if b < menor_valor or i == 0:
        menor_valor = b
    b = (b,)
    a = a + b
print(f'Os números sorteados foram {a}, o maior valor foi {maior_valor} e o menor {menor_valor}.')
