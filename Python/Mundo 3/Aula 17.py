# Aula sobre listas.
# Para adicionar itens a uma lista, usa-se listaemquestão.append()
a = ['a,', 'b', 'c, d']
a.append('e')  # Adicione 'e' como o último índice da lista.
print(a)
#  Caso você queira adicionar algum item em um ponto específico, use insert()
a.insert(1, 'f')
a.insert(0, 'lolo')
print(a)
del a[1]  # Del é uma declaração e pode remover outras coisas, inclusive tuplas.
a.remove('lolo')  # Mas tuplas remove integralmente.
a.pop()
a.pop(2)
print(a)
#  Criando lista a partir de um range
valores = list(range(0, 9))
print(valores)
valores.sort(reverse=True)
print(valores)
b = [0, 3, 9, 2, 5, 4, 18, 21, 9, 0]
b.sort()  # Ordenação da lista. Método in place não vai direto no print.
print(b)
print(len(b))
# Você pode trocar o valor de um índice em uma lista:
c = [0, 1, 2]
print(c)
c[0] = 9
print(c)
# Uma lista vazia pode ser feita de duas formas:
k = list()
o = []
# Um outro exemplo:
for i, j in enumerate(b):
    print(f'Na posição {i+1} temos {j}.')
# É possível fazer uma cópia de uma lista em outra, mas não como
# no caso das tuplas. Se fizer a = b, liga-se a lista a com b, enquanto
# em tuplas, temos que a tupla b copiou a tupla a, mas se você modificar
# uma ou outra, uma ou a outra permanecerá inalterada.
# Para realizar a cópia, usa-se o método copy()
d = [0, 1]
ff = d.copy()
ff.append(1)
print(ff)  # Agora as listas podem ser modificadas de modo independente
print(d)
# Exercícios do 78 ao 85.
