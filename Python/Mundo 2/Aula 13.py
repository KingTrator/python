a = 'Oi'
for i in range(1, 6):
    print(a, end='')
# ou
print('\n')
for i in range(1, 6):
    print(a, end='|')
    b = i * 2
    print("O dobro de", i, "é", b, end='|')
# Se você quiser contar números, pulando-os ou de trás para frente, faça:
print('\n')
for i in range(3, -1, -1):
    print(i, end='|')
print('\n')
# Se você quiser que o usuário defina o looping, você pode fazer:
n = int(input('Digite um número: '))
nn = int(input('Digite um número: '))
passo = int(input('Defina um passo'))
# obs: o passo é o espaçamento do looping

for i in range(n, nn + 1, passo):
    print(i)
print('FIM')
# Note que no Python a contagem começa em 0 e ignora o último valor,
# por isso eu devo fazer nn + 1 para contar todos os valores digitados.





# A razão de no segundo caso sair uma coluna de "oi" é porque a função
# "print", por padrão, adiciona um espaço.
# Este i eu não sei bem o que significa, mas é necessário usá-lo
# caso não queira que a variável seja transformada em números.
# obs: não é preciso usar i, pode ser qualquer outra variável.
# Pelo que entendo, então, i é a variável maior na qual colocamos um loop.
# Dentro dessa variável maior (DENTRO DO LOOP), podemos colocar outras
# variáveis, como "a" em print(a).
