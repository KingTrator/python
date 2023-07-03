# Vou manter o exercício da maneira que resolvi originalmente,
# mas preciso deixar a versão reduzida... que é muitooo reduzida em relação
# ao tralálá que fiquei fazendo.

num = int(input('Digite um número para ver a tabuada dele: '))
for i in range(1, 11):
    print(f'{i} x {num} = {num*i}') # Note que o print já vem com /n "embutido".









print('\033[1;31m BEM VINDO A TABUADA SUPREMA - DIGITE QUALQUER NÚMERO PARA'
      ' ENCONTRAR SUA RESPECTIVA TABUADA. \033[m')
n1 = int(input('Digite um número: '))
for i in range(1, 10):
    k = n1 * i
    if 0 <= i < 9 and k < 10**9:
        print(k, end='||')
    elif k >= 10**9:
        str_k = str(k)
        if len(str_k) >= 9:
            print(k, '\n')
    elif i == 9:
        print(k, end='')
# Eu resolvi deixar o meu primeiro código deste jeito mesmo, só para provar
# que funciona a conversão de k para str e depois a verificação do total
# de caracteres pela função len, que, por conta das outras condições,
# necessariamente retornará como verdadeiro if len(str+k) >= 9: e dará
# um print tipo print(k, '\n'), a fim de evitar que números grandes sejam
# todos colocados em uma mesma linha, o que dificultaria a visualização
# do código.
# No entanto, uma versão mais pratica desse código é:
print('\n')
print('\033[1;31m BEM VINDO A TABUADA SUPREMA - DIGITE QUALQUER NÚMERO PARA'
      ' ENCONTRAR SUA RESPECTIVA TABUADA. \033[m')
x = int(input('Digite o inteiro que deseja ver a tabuda:'))
for i in range(1, 10):
    l = x * i
    if 1 <= i < 9:
        print(l, end='||')
        if l >= 10**9:
            print(l, '\n')
    elif i == 9:
        print(l, end='')


