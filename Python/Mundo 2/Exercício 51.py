print('\033[1m MOSTRAR 10 PRIMEIROS TERMOS DA PA E SUA RAZÃO \033[m')
p = float(input('Digite a razão da PA: '))
a1 = float(input('Qual o primeiro termo da PA? '))
# A razão de criarmos uma outra variável para armazenar a1 é que queremos manter
# a variável a1 para poder printá-la ao final do código sem as alterações do loop.
termo = a1
# Em vez de ficar definindo o intervalo da função loop, posso apenas dizer quantos
# loops serão feitos.
print('Abaixo, os dez primeiros termos da PA de razão {:.2f}'.format(p))
for i in range(10):
    if i == 0:
        print(a1, end='||')
    else:
        termo += p
        print('{:.2f}'.format(termo), end='||')
# O GPT-4 me fez perceber que este código pode ser otimizado.
# As condicionais são dispensáveis. Basta que eu elimine "termo = a1" e coloque
# o print para ser executado antes de a1 +=, pois isso fará com que primeiro
# o print seja de a1 da forma que está no Input. Na sequência, a1 recebe a1 + p
# e então se conclui o primeiro laço. No segundo laço, o print de a1 resultará em
# a1 == a1 + p, então haverá uma nova modificação em a1, que agora recebe
# de novo a1 + p, tornando-se, assim, a1 == a1 + p + p
print('\033[1m MOSTRAR 10 PRIMEIROS TERMOS DA PA E SUA RAZÃO \033[m')
p = float(input('Digite a razão da PA: '))
a1 = float(input('Qual o primeiro termo da PA? '))
print('Abaixo, os dez primeiros termos da PA de razão {:.2f}'.format(p))

for i in range(10):
    print('{:.2f}'.format(a1), end='||')
    a1 += p
