n1 = float(input('Digite um número: '))
n2 = float(input('Digite um número: '))
n3 = float(input('Digite um número: '))
if n1 > n2 and n1 > n3:
    print('{} is the largest number.'.format(n1))
if n1 < n2 and n1 < n3:
    print('{} is the smallest number.'.format(n1))
if n2 > n1 and n2 > n3:
    print('{} is the largest number.'.format(n2))
if n2 < n1 and n2 < n3:
    print('{} is the smallest number.'.format(n2))
if n3 > n2 and n3 > n1:
    print('{} is the largest number.'.format(n3))
if n3 < n2 and n3 < n1:
    print('{} is the smallest number.'.format(n3))
# O código está 100%. O "weak warning" que é sinalizado se refere aos comentários
# que estou deixando aqui. Abaixo, coloco o código prévio que havia tentado montar
# fracassadamente. (O weak warning chama para a PEP 8 que é um monumento de referência
# a como trabalhar com códigos em Python. Segundo a PEP 8, comentários devem ser
# colocados, preferencialmente, em cima dos códigos de referência e não abaixo ou dos lados.
# No entanto, neste caso, eu estou usando isso como um lembrete, então a regra não se encaixa.
# # O código abaixo NÃO FUNCIONA!
# # print('Comparemos três números distintos quaisquer.')
# # a = float(input('Digite um número qualquer: '))
# # b = float(input('Digite um número qualquer: '))
# # c = float(input('Digite um número qualquer: '))
# # k = a/b
# # p = a/c
# # l = b/c
# # if a == b == c:
# #     print('Você digitou os mesmos números.')
# # elif a == b or a == c or b == c:
# #     print('Dois dos números são iguais, escolha três distintos.')
# # elif k > 1 and p > 1:
# #     print('{} é o maior dos números.'.format(a))
# # elif k > 1 and l < 1:
# #     print('{} é o menor dos números.'.format(b))
# # elif k < 1 and p < 1:
# #     print('{} é o menor dos números.'.format(a))
# # elif k < 1 and l > 1:
# #     print('{} é o maior dos números'.format(b))
# # elif l < 1 and p < 1:
# #     print('{} é o maior dos números'.format(c))
# # else:
# #     print('{} é o menor dos números'.format(c))
# # # Versão corrigida
# # print('Comparemos três números distintos quaisquer.')
# # a = float(input('Digite um número qualquer: '))
# # b = float(input('Digite um número qualquer: '))
# # c = float(input('Digite um número qualquer: '))
# #
# # if a == b:
# #     print('Dois dos números são iguais, escolha três distintos.')
# # elif a == c:
# #     print('Dois dos números são iguais, escolha três distintos.')
# # elif b == c:
# #     print('Dois dos números são iguais, escolha três distintos.')
# # else:
# #     if a > b:
# #         if a > c:
# #             print('{} é o maior dos números.'.format(a))
# #             if b < c:
# #                 print('{} é o menor dos números.'.format(b))
# #             else:
# #                 print('{} é o menor dos números.'.format(c))
# #         else:
# #             print('{} é o maior dos números.'.format(c))
# #             print('{} é o menor dos números.'.format(b))
# #     else:
# #         if b > c:
# #             print('{} é o maior dos números.'.format(b))
# #             if a < c:
# #                 print('{} é o menor dos números.'.format(a))
# #             else:
# #                 print('{} é o menor dos números.'.format(c))
# #         else:
# #             print('{} é o maior dos números.'.format(c))
# #             print('{} é o menor dos números.'.format(a))

# Além disso, há outra maneira, mais simplificada, de executar o código.
print('\n')
print('Hello World!')
x1 = float(input('Enter a number: '))
x2 = float(input('Enter a number: '))
x3 = float(input('Enter a number: '))
largest = max(x1, x2, x3)
smallest = min(x1, x2, x3)
print('{} is the largest among the three numbers entered'.format(largest))
print('{} is the smallest among the three numbers entered'.format(smallest))