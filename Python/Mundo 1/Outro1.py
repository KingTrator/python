n1 = input('Digite um número:')
print('\033[1;31;46m',type(n1),'\033[m')
# O código está executando e funcional. Note que "type", na função print
# pede ao python que diga qual é a classe da variável "n1".
# Como n1 está dentro de uma string ' ', lesse que é uma palavra ou string.
# Para que a leitura correta de type fosse que se trata de um número inteiro
# ou não, seria necessário colocar "input" dentro de "float" ou "int".
n2 = int(input('Digite um número'))
print('\033[7;32;33m',type(n2),'\033[m')
# Agora o programa detecta que se trata de um int, númeor inteiro (se você
# digitar um número float, ainda assim seria detectado como int, porque a função
# é int).

# Após terminar o Mundo 1 de Python, voltei para adicionar cores, conforme
# a última aula do curso :)
