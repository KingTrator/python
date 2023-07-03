import moeda
# Exercício Python 109: Modifique as funções que foram criadas no desafio 107 para
# que elas aceitem um parâmetro a mais, informando se o valor retornado por elas vai ser ou não
# formatado pela função moeda(), desenvolvida no desafio 108.
print('-='*40)
print('Olá, sejá bem vindo a \033[1;33mANÁLISE (SIMPLES) DE VALOR\033[m')
print('Espero que as análises propostas ao valor inserido lhe seja útil')
print('-='*40)
valor = float(input('Digite um valor: '))
print(f'Para o valor digitado {moeda.moeda(valor, neutral=True)}, há os seguintes resultados: ')
print(f'Um aumento de 10% em {moeda.moeda(valor)} = {moeda.aumentar(valor)}')
print(f'O dobro de {moeda.moeda(valor, neutral=True)} = {moeda.dobro(valor, neutral=True)}')
print(f'Uma redução de 10% em {moeda.moeda(valor)} = {moeda.diminuir(valor)}')
print(f'\033[1mVOLTE SEMPRE')
