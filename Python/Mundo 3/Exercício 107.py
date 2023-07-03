import moeda
# Exercício Python 107: Crie um módulo chamado moeda.py que tenha as funções
# incorporadas aumentar(), diminuir(), dobro() e metade(). Faça também um programa que
# importe esse módulo e use algumas dessas funções.


print('-='*40)
print('Olá, sejá bem vindo a \033[1;33mANÁLISE (SIMPLES) DE VALOR\033[m')
print('Espero que as análises propostas ao valor inserido lhe seja útil')
print('-='*40)
valor = float(input('Digite um valor: '))
print(f'Para o valor digitado R${valor}, há os seguintes resultados: ')
print(f'Um aumento de 10% em R${valor} = {moeda.aumentar(valor)}')
print(f'O dobro de R${valor} = {moeda.dobro(valor)}')
print(f' A metade de R${valor} = {moeda.metade(valor)}')
print(f'\033[1mVOLTE SEMPRE')

# Originalmente, moeda.qualquerfunção retornava apenas o float com "." marcando casas decimais, mas como
# modifiquei o módulo moeda.py para o Exercício 108, aqui também ocorreu uma transformação.
# Por isso você verá algumas inconsistências nas respsotas dadas.
