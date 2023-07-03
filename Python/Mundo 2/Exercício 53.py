nome = input('Digite uma frase ').replace(' ', '').lower()
len_nome = len(nome)
for i in range(len_nome//2):
    if nome[i] != nome[len_nome - i - 1]:
        print('A frase não é um palíndromo.')
        break
else:
    print('É um palíndromo!')
# Não é preciso, no entanto, usar laço para verificar se a palavra
# é ou não um palíndromo, isso especificamente no PYTHON.
# Também é válido:
inverso = nome[::-1]  # Aqui você tem o inverso da frase.
# Retirando espaços e deixando as letras de mesmo tamanho, basta
# fazer # if inverso == len_nome e dar os respectivos prints.
print(inverso)