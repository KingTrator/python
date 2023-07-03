import random
a = 'Ana'
b = 'Bruno'
c = 'Carlos'
d = 'Diana'

var = random.choices([a, b, c, d])
print('\033[1m', var, '\033[m')
# Novamente precisei da ajuda do chatGPT-3.5. Neste caso, não sabia que era
# preciso usar [ ] colchetes nesta função. No caso, o Python entende, com os colchetes
# que os argumentos a, b c e d são itens de uma lista. Sem eles, ele lê todo o conteúdo
# das variáveis e, assim, seleciona uma única letra dentre as presentes nas variáveis.
print('{}'.format('\033[45m'), '  '*60, '{}'.format('\033[m'))
H = ['Ana', 'Bruno', 'Carlos', 'Diana']
P = random.shuffle(H)
print('\033[1m Vejamos agora a ordem dos alunos.')
print('Ordem dos alunos {}.'.format(H))

# O chatGPT-3.5 me explicou a diferença entre [ ] e ( ) no Python.
# Os colchetes servem para separar listas e símiles, enquanto os parênteses
# servem para separar tuplas e símiles.
# E o que são tuplas? Tuplas são como se fossem orações independetes. Elas
# Não podem ter a ordem alterada. Por outro lado, as listas são como uma sequência
# de adjetivos, cuja ordem não é tão importante e está sujeita a alteração.
# Por isso mesmo, para usar a função random para qualquer coisa, é preciso usar
# [ ], pois isso será interpretado como algo passível de mudança, enquanto os ( )
# tratam de itens que não devem ser mudados, resultando em erro.
