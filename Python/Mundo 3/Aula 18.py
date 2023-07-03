# Cuidados com append(). Ele cria uma ligação entre duas listas.
# Se você modificar uma, também modificará outra.
# Ex:
list = ['Gustavo', 40]
lost = []
lost.append(list)  # As listas estão ligadas.
list[0] = 'Fernanda'
list[1] = '19'
print(lost)
# Correção:
x = ['Gustavo', 40]
y = []
y.append(x[:])  # cópia de uma lista em outra, listas não ligadas.
x[0] = 'Fernanda'
x[1] = 19
y.append(x[:])
print(y)
# Exercícios do 84 ao 89