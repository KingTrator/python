# Procurando pela letra A.
frase = input('Digite algo: ')
aumento = frase.upper() # Observação: sem o parênteses, eu chamo o método em si e não sua função, mas não sei bem o que isso significa.
v1 = aumento.find('A')
contar = aumento.count('A')
v2 = aumento.rfind('A')
print('Em {} a letra A aparece pela primeira vez em {}, pela última em {} '
      'e por um total de {} vezes.'.format(frase, v1, v2, contar))
print(len(frase)) # O len conta a partir do 0, mas dará o númeor correto de caracteres.
# É possível tornar o código mais amigável para o usuário visualiza.
FF = input('Digite algo: ').strip()
ff = FF.upper()
print('Não importa o porquê, mas o A aparece pela primeira vez no caracter'
      '\n {}, pela última vez em {}, por um total de {} vezes.'.format(ff.find('A') + 1, ff.rfind('A') + 1, ff.count('A')))
# Ainda há imprecisões,mas é o que posso fazer no meu nível atual.

# 2
name = input('Digite o seu nome completo').strip
name = name.split()
l1 = name[0]
l2 = name[-1]
print('O seu primeiro nome é {}, o seu último nome é {}.'.format(l1, l2))
# 0 é para pegar o primeiro, 1 para pegar o segundo, 2 para pegar o terceiro...
# -1 é para pegar o último, -2 é para pegar o penúltimo, -3 é para pegar o antepenúltimo.

# O código está funcional.
