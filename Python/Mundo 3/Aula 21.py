# Para obter informações sobre funções e qualquer coisa do Python,
# pode-se usar help() em uma aba como esta, na qual você terá várias
# informações ou usar o doc. As informações entre eles são levemente distintas.
# print(input.__doc__) Opção 1 (Guanabara não recomenda)
# help() Opção 2 (Guanabara recomenda) ou help(itemquevocêquersaber)
# Caso você queira documentar no help uma função que tenha criado por
# meio de def, basta usar as docstrings. Abaixo, um exemplo.
# Para visualizar o exemplo, retire o comentário

#def contador(a):
    #"""
    #:param a: Valor de partida para a contagem regressiva
    #:return: Sem retorno
    #Criado por King Trátor, minha primeira docstring.
    #"""
    #b = a
    #if a < 0:
    #    a = a * (-1)
    #for i in range(a+1):
    #    print(b, end=' ')
    #    b -= 1


#help(contador)
# Parâmetros opcionais, basta colocá-los como c = 0. Veja:
def somar(a, b, c=0, d=0):
    s = a + b + c + d
    print(s)
# Nesse def, você não precisa digitar c e d e a soma não será comprometida.
somar(1, 2)
somar(1, 2, 3)
somar(1, 2, 3, 4)

# Há poucas horas, o GPT havia comentado comigo sobre escopo global
# e escopo local.
# Nesta aula eu vejo mais sobre isso.
# No escopo global, variáveis estão fora de quaisquer funções e por
# isso funcionam em todo o programa.
# Por outro lado, variáveis locais são aquelas que estão dentro de
# uma ou mais funções, mas o valor delas não é globalmente atribuído.
# Ou seja, você não obterá nada se tentar usá-la fora de def, exceto
# se defini-la fora de def.
# Note:
n = 0  # Exemplo de variável global


def mostra():
    x = 1  # Exemplo de variável local
    print(x)    # Retona 1
    print(n)    # Retona 0
#print(x)    # Dá erro
print(n)    # Retorna 0, pois é anterior a função teste. Isso faz sentido
            # pois o Python lê o código de cima para baixo, na ordem.

# Caso você não queira usar a variável local, mas uma gloal,
# basta escrever isto:
def teste():
    global n
    n = 1   # n é definida globalmente como 1
    print(f'{n}')   # retorna 1


teste()
print(n)  # retorna 1
# Uso de return


def summer(a =0, b=0, c=0):
    s = a + b + c
    #print(s) Nesse caso, toda vez que summer for chamada, irá
    # dar um print com quebra de linha. Isso pode ser ruim para quando
    # se deseja realizar uma formatação própria. Uma maneira de evitar isso
    # é por isso de return s, desse modo o s será armazenado em uma variável,
    # a qual deverá ser definida pela pessoa.
    # Na verdade, convenhamos, é isso que eu venho feito desde o começo do
    # curso. Antes, eu me perguntava porque não dava para chamar uma função
    # por si própria, (e na real uma delas até dava, a sleep()), mas
    # agora eu entendo, é porque nelas vem essa idea de return.
    return s


r1 = summer(1, 2, 3)
r2 = summer(1, 2)
r3 = summer(1)
print(f'O valor das variáveis r1, r2 e r3 é, respectivamente, {r1}, {r2}, {r3}.')
# Ao contrário de algumas outras linguagens de programação, Python permite que
# as funções retornem valores de qualquer tipo, não apenas booleanos ou números.
# Isso inclui listas, dicionários, outros objetos e até mesmo outras funções.