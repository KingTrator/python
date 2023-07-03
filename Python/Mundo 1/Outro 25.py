# 1
N = input('\033[1mQual o seu nome?\033[m').strip()
# Caso queira deixar a função ativa para todo script, basta não fechá-la com \033[m
print('{}'.format('\033[4m'), N.upper())
print(N.lower())
# K = N.replace(' ', '') - o código fica mais econômico se eu usar esta função dentro de .format
X = N.split()
L = X[0]
print('Seu nome completo possui {} letras'.format(len(N.replace(' ', ''))))
print('Seu primeiro nome possui {} letras.'.format(len(L)))

#Alternativa de resolução:
# N = input('Qual o seu nome?').strip()
# ...
# print('Seu nome completo possui {} letras'.format(len(N) - N.count(' '))
# Essa segunda solução eu já havia achado em um primeiro momento, mas como não
# havia usado o ".strip" em N naquela vez, pensei que poderia dar erro caso o espaço
# (e daria mesmo) viesse antes do nome. No entanto, com a função strip ativada,
# é garantia que:
# print('Seu primeiro nome possui {} letras.'.format(N.find(' '))
# dará o número de letras correto.
# Mas o meu código tem uma vantagem: ele é mais flexível. Se eu decidir saber qual é
# o segundo nome ou terceiro nome, posso modificá-lo a qualquer momento.

# 2
print('\n \n')
# Embora eu queira que a pessoa digite um número, estou realizando manipulações textuais,
# assim, para que o Python possa realizá-las, eu preciso tratar o número como se fosse
# uma string.
numero = (input('Digite um número entre 0 e 9999: '))
numero = numero.zfill(4) # Essa função foi uma novidade, sem ela, não teria resolvido o exercício.
milhar = numero[0]
centena = numero[1]
dezena = numero[2]
unidade = numero[3]
print('O milhar é {}, a centena é {}, a dezena é {} e a unidade é {}'.format(milhar, centena, dezena, unidade))
print('\n \n')
# Existe uma maneira muito mais sofisticada de resolver esse exercício, matematicamente
# falando. Não é preciso usar zfill, que, de fato, facilita muito a vida.
# A solução elegante é:
num = int(input('Digite um número entre 0 e 9999: '))
u = num % 10 # Veja que interessante:
# no caso, eu divido por um para manter o número integral (nem precisa, até tirei). Depois eu pego o resto
# da divisão por 10. Aqui entra a parte matemágica: o resto da divisão por 10 é
# a própria unidade, em qualquer caso, haja vista que qualquer número AB por dez
# sobra´ra apenas AB pois 1 . n = A e 0 . X = 0 e B - 0 = 0.
# Assim sendo, posso replicar a ideia para as demais variáveis!!
d = num // 10 % 10  # Aqui eu faço a divisão inteira do valor. Se for ABDC, ficará só ABD.
c = num // 100 % 10
m = num // 1000
# Na real, para "u" e "m" eu posso simplificar o código. Isso porque o resto
# da divisão de qualquer número por 10 é a própria unidade desse número.
# Já para "m", vem que a divisão inteira de um milhar por 1000 será o próprio
# milhar. Por outro lado, se o valor for inferior a um milhar (1000), a resposta
# será 0, o que continua permitindo que o código funcione.
# Fico feliz, afinal, eu encontrei uma solução mais simples que a do professor (que se
# propunha a mostrar sempre os códigos mais curtos).
print('O milhar é {}, a centena é {}, a dezena é {} e a unidade é {}'.format(m, c, d, u))

