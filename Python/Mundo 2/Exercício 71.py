# Este código está mais longo do que o necessário. Procure simplificá-lo em até 25 linhas... Mantendo os enfeites.
print('=' * 20)
print('CAIXA ELETRÔNICO SUCURI')
print('=' * 20)
pido = int(input('Qual valor você deseja sacar? R$ '))
n = pido
c50 = c20 = c10 = c5 = c1 = 0
while True:
    if c50 < 12 and n >= 50:
        c50 += 1
        n -= 50
    elif c20 < 12 and n >= 20:
        c20 += 1
        n -= 20
    elif c10 < 12 and n >= 10:
        c10 += 1
        n -= 10
    elif c5 < 12 and n >= 5:
        c5 += 1
        n -= 5
    elif c1 < 12 and n >= 1:
        c1 += 1
        n -= 1
    limite = c1 + c5 + c10 + c20 + c50
    if n == 0 or limite >= 60:
        break
if limite < 60:
    print(f'Ao sacar R${pido} você receberá {c50} notas de 50, {c20} de 20, {c10} de 10, {c5} de 5 e {c1} de um real')
else:
    print('O valor inserido ultrapassa o limite de cada tipo de nota que podemos disponibilizar.'
          '\n Pedidmos por sua compreensão e que solicite atendimento especializado.')
