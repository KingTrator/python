import re
# Encontrando Padrões de Texto: Imagine que você tem uma lista de palavras e precisa encontrar
# todas as palavras que começam com a letra 'a' e terminam com a letra 'm'. Usando expressões regulares em
# Python, como você faria isso? Crie um script para solucionar este problema.
# Lembre-se de usar o módulo re em Python e a função re.search para isso.
words = ['am', 'album', 'arm', 'battle', 'calm', 'dam', 'earn', 'am', 'amy']
# Sua solução aqui:
lista = list()
for word in words:
    x = re.findall('^a.*m', word) # select all the excerpts that start with a and have a m.
    lista.append(x)  # save x into a list
    if not x:  # If x = [], delete the last x added
        lista.pop()
    elif x != [word]: # If x does not match word, delete the last x from the list.
        lista.pop()
print(lista)

