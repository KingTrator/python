import moeda
# Exercício Python 108: Adapte o código do desafio #107, criando uma função adicional
# chamada moeda() que consiga mostrar os números como um valor monetário formatado.

print('-='*40)
print('Olá, sejá bem vindo a \033[1;33mANÁLISE (SIMPLES) DE VALOR\033[m')
print('Espero que as análises propostas ao valor inserido lhe seja útil')
print('-='*40)
valor = float(input('Digite um valor: '))
print(f'Para o valor digitado {moeda.moeda(valor)}, há os seguintes resultados: ')
print(f'Um aumento de 10% em {moeda.moeda(valor)} = {moeda.aumentar(valor)}')
print(f'O dobro de {moeda.moeda(valor)} = {moeda.dobro(valor)}')
print(f'Uma redução de 10% em {moeda.moeda(valor)} = {moeda.diminuir(valor)}')
print(f'\033[1mVOLTE SEMPRE')
