# Vamos contar apenas as palavras de uma frase, sem contar os espaços.
F = ('Olá, eu sou um amendobobo, bobo YEAH')
Ff = F.split()
print(len(Ff))

# Agora vamos supor que você queira fazer uma brincadeira com um jogador de um jogo
# +18. Ele deverá escolher o nome do personagem, que necessariamente deve ser 18+
# mas você deixa ele por qualquer número, 17, 16... 0 anos. No entanto,
# ao fazer isso, o nome será mudado para 18 de toda forma.
idade = ('13')
idade = idade.replace('13','18')
print('Certo, você tem {} anos.'.format(idade))

# Claro que isso é para um valor fixo, mas podemos criar condições.
ID = int(input('Qual a sua idade?'))
if ID < 18:
    ID = 18
print('Certo, você tem {} anos.'.format(ID))
# Neste caso, se o usuário resolver dizer que o próprio personagem é menor de idade
# o script retornará o mínimo da idade legal (18 anos). Se a idade for 18 anos
# ou mais, então ele retornará a idade escolhida.
