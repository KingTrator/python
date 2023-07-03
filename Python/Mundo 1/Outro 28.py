nota = float(input('Digite sua primeira nota: '))
note = float(input('Digite sua segunda nota: '))
m = (nota + note)/2
if 4.5 <= m <= 6:
    print('Você precisa se dedicar mais')
elif 1 <= m < 4.5:
    print('Ei! Aconteceu alguma coisa? Sua nota está muito baixa. Vamos conversar.')
elif 0 < m < 1:
    print('Isso é preocupante.')
elif m == 0:
    print('0? Ok, você não estudou.')
elif 6 < m  < 8:
    print ('Parabéns, você está no caminho.')
elif 8 < m < 9:
    print('Uau! Que notão!')
elif 9 < m < 10:
    print('Você quase gabaritou!! Uhuuul!')
else:
    print('Queria que você fosse meu filho :)')

