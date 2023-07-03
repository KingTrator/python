# Estudo sobre tuplas.
# Eu já conheço um pouco sobre tuplas e listas (próxima aula) porque
# alguns dos exercícios do mundo 2 eram mais bem resolvidos por meio de uma
# ou de outra e o GPT-4 comentou isso comigo e deu alguns exemplos, além
# de que o próprio Guanabara fez observações.
# Ainda assim, esclareçamos:
# 1. Tuplas são imutáveis
# 2. Podemos localizar elementos na tupla das seguintes formas:
# 2.1 [1:] todos, a partir do zero (este incluso), mas sem o índice 0.
# 2.2 [3:] a partir do 3 (este incluso) até o final.
# 2.3 [:3] até antes do três (o último não é contado).
# 2.4 [1:3] do 1 até o 3, exceto o 3.
# 2.5 [-1] o último.
# 2.6 [-2] o penúltimo.
# 2.7 [-2:] Todos exceto o último e o penúltimo.
a = 'cachorro', 'batata', 'saco', 'queisso',  # Duplas são demarcas por aspas simples + , como no exemplo, há 4.
print(a[:-2])
# 3. Pode-se usar o len() em tuplas.
# 4. Posso usar o for com o range ou com o len da tupla:
for i in range(0, len(a)):
    print(a[i])
for i in a:
    print(a)  # Ele pula índice a índice sozinho
# Quando precisar mostrar a posição do item na tupla, usamos o enumerate:
for i, j in enumerate(a):
    print(f'Temos {j} na posição {i}')
# 5. Posso usar o sorted para ordernar uma tupla.
# 5.1 Tuplas apenas str são ordenadas em ordem alfabétca.
# 5.2 Tuplas numéricas são ordenadas em ordem crescentes.
# 5.3 Sorted é uma função, então há métodos que permitem variações.
print(sorted(a))
b = '5', '2', '34', '1', '99'
print(sorted(b))  # Emborao os números estejam em str, ele os reconhece.
# 6. Posso concatenar tuplas:
c = a + b  # Aqui eu mesclo as tuplas em uma única
print(c)
c = a, b  # Aqui eu coloco duas tuplas em uma tupla maior.
print(c)
# 7. Posso encontrar algum item por meio da função index()
print(a.index('cachorro'))
print(b.index('2')) # O index pega sempre a PRIMEIRA ocorrência
d = 1, 2, 3, 4, 5, 5, 5, 5, 6
# Posso analisar a partir de uma posição em específico:
print(d.index(5, 7))  # procurar por 5 a partir da posição 7.
# 8. Tuplas podem ter diferentes tipos de dados:
e = ('a', a, 1)
print(e)
# 9. Posso usar a função "del" para apagar qualquer coisa no Python...
# inclusive as tuplas. A tupla não, não elementos específicos.
del(e)
print(e)  # Aqui aparecerá um erro: e não está definido.
# Exercícios do 72 ao 77
