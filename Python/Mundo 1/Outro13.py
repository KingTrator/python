
#print(emoji_list.money, emoji_list.money, emoji_list.money, emoji_list.money)
#Primeira biblioteca do Pypi oficialmente importada.

from emoji import emojize
print('\033[1;31;41m', emojize(":money_bag:")*5, '\033[m')
#Essa aqui funciona melhor que a emoji_list
print('\n \n \n')
# O chatGPT deu-me essa solução para o meu problema com a lista de emojis.
# Aparentemente [n] em que n é um número inteiro seleciona apenas o item que está
# na posição n (n = 0 é 1ª posição) para o código, pois nesse caso, emoji_list é
# chamada de LISTA enquanto emoji é DICIONÁRIO. Quando a biblioteca é um dicionário
# posso procurar nela, exemplo BIBLIOTECA.qualquercoisa, aquilo que desejo, enquanto
# no caso de listas, ao menos uma das maneiras, eu devo ou pegar todos os emojis
# ou selecioná-los em [n].
# print(emoji_list.money[3])
# print('\n \n')
# Além disso, para imprimir várias vezes o mesmo emoji, basta, dentro do parênteses
# multiplicá-lo.
# print(emoji_list.money[3]*10)

# O código está operando e funcional. Thank GOD... thank chatGPT-4.