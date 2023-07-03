# Aqui estou aprendendo outras formas de quebrar linha, como já aprendi anteriormente
# além de formas de não a quebrar e não a quebrar com modificações.

n1 = int(input('Digite algo'))
n2 = int(input('Outra coisa'))
s = n1 + n2
m = n1 * n2
p1 = n1 ** n2
p2 = n2 ** n1
d = n1 / n2
di = n1 // n2
r = n1 % n2
print('A soma é {}, o produto é {}, a potência n1 sob n2 é {}, a potência'
      '\nn2 sob n1 é {}, a divisão é {}, a divisão inteira é {} e o resto é {}'.format(s, m, p1, p2, d, di, r))

# Não consegui executar o código quando dei um \n para quebrar a linha e escrever, ao fim, .format
# aparentemente, o .format deve estar sempre ao lado da última string, ainda que não fique
# visível,como é o caso deste aqui.

#Fazendo uma variação do código:

l1 = int(input('Digite algo'))
l2 = int(input('Digite outra coisa'))
sl = l1 + l2
ml = l1 * l2
dl = l1 / l2
dil = l1 // l2
pl = l1 ** l2
print('Na ordem em que se foi digitado, a soma é {}, a multiplicação é {}'.format(sl, ml), end='||')
print('A divisão é {:.3f}, a divisão inteira é {} e a potência é {}'.format(dl, dil, pl))
#Pelo que estou entendendo o ":" marca alguma informação a ser adicionado no {} 3f significa
# 3 casas decimais, ao menos isso.

print('Na sequência, as mesmas respostas, mas sem o uso da função end e sim com'
      'quebras usando barras (\)')

print('Na ordem em que se foi digitado, \n A soma é {}\n A multiplicação é {}'.format(sl, ml), end=' ')
print('\n A divisão é {} 6\n A divisão inteira é {} \n A potência é {}'.format(dl, dil, pl))
# As respostas da divisão neste código (talvez) variam em relação ao anterior, pois não usei
# {:.3f} para delimitar o número de casas decimais.
#Inserir um :4 ou :20 significa o número de espaços na máscara, ainda que
#o que estiver inserido não contemple todos esses espaços.










