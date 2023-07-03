#N = float(input('{}Digite um número real qualquer, com casas decimais:{} '.format('\033[1;31;45', '\033[m')))
N = float(input('{} Digite um número qualquer:{} '.format('\033[1;41m', '\033´m')))
M = int(N)
print('{} O número {:^10} possui como parte inteira o {:^10}.{}'.format('\033[1;41m',N, M, '\033[m'))


# Naturalmente, é desnecessário o :^10 que coloquei dentro das máscaras,
# mas como não costumo usar essa "função", achei que seria bom deixá-la por aqui,
# por questão de treino. Eventualmente poderá ser útil lembrar disso.





