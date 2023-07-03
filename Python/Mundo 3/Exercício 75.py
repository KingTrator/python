# O código deverá dizer quantas vezes o número 9 foi digitado.
# Deverá dizer quais foram os pares digitados.
# Deverá armazenar os números em uma tupla.
# Deverá dizer o índice do primeiro 3 a ter sido digitado.
v = ()
c = 0
a = ()
for i in range(4):
    b = (int(input('Digite um inteiro: ')))
    if b % 2 == 0:
        a = a + (b,)
    v = v + (b,)
    if b == 9:
        c += 1
if c >= 1:
    print(f'O número 9 foi digitado {c} vez(es).')
else:
    print('O número 9 não foi digitado nenhuma vez.')
if 3 in v:
    print(f'O número 3 aparece na tupla pela primeira vez no índice: {v.index(3)}.')
else:
    print('O 3 não foi digitado.')
if a != ():
    print(f'Os números pares digitados foram {a}.')
else:
    print('Não foram digitados números pares.')
# O código ficou muito longo. Vou deixá-lo aqui, porém, apenas porque ele é mais
# adaptável, isto é, posso digitar apenas 4 números, mas posso digitar muito mais, o que
# é uma versatilidade interessante.
# Abaixo, uma versão mais simples:
num = (int(input('Digite um número: ')),  # Torna núm uma tupla.
       int(input('Digite um número: ')),
       int(input('Digite um número: ')),
       int(input('Digite um número: ')))  # Fecha a tupla de 4 itens.
print(f'Você digitou {num}')
K = ()
for i in range(len(num)):
    if num[i] % 2 == 0:  # Cuidado!!
        K += (num[i],)  # Cuidado!!
R = num.count(9)
if 3 in num:  # Tentei com if num.index(3) is True, mas não deu.
    print(f'{R} vez(es) foi digitado o nove.')
    print(f'O três aparece pela primeira vez na posição {num.index(3) + 1}.')
    print(f'Os números pares digitados são {K}.')
else:
    print(f'{R} vez(es) foi digitado o nove.')
    print(f'Os números pares digitados são {K}.')
