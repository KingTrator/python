#O objetivo deste teste é verificar que .format pode ser, muitas vezes, mais
# eficiente do que o uso de "," ou "+". Observe.
n1 = int(input('\033[4;33;40mDigite um número:\033[m '))
n2 = int(input('\033[4;33;40mDigite um número:\033[m '))
s = n1 + n2
print('{}A soma entre {} e {} é {}.{}'.format('\033[4;33;40m', n1, n2, s, '\033[m'))
#Comparativamente, sem o uso da máscara {}, teríamos de realizar o código:
n3 = int(input('{}Digite um número:{} '.format('\033[1;4;32;40m', '\033[m')))
n4 = int(input('{}Digite um número:{} '.format('\033[1;4;7;37;40m', '\033[m')))
ss = n4 + n3
print('\033[7;37;44m','A soma entre', n3, 'e', n4, 'é', ss, '\033[m')
#Agora verifiquemos o uso de valores boleanos, função bool.
print('{} A soma dos valores retorna em booleano: '
      '{}{}{}.{}'.format('\033[1;31;45m','\033[1;7;32;40m', bool(ss),'\033[m', '\033[m'))
