#Aqui estou trabalhando algumas funções extras da função print, as quais incluem
# o conhecimento sobre formas de alinhamento.
nm = input('Olá, qual o seu nome?')
print('Prazer em te conhecer {:40}!'.format(nm))
#No exemplo de cima, os dois : servem para marcar alguma alteração de alinhamento
#sobre a máscara. :40 significa que a máscara deve ser escrita em 40 espaços.
# Caso o nome tenha menos de 40 espaços, haverá, ainda assim, 40 espaços marcados,
#isto é, o "!", que vem depois, é jogada 40 espaços da máscara (nm).

K = input('Digite algo')
print('Você digitou isto: {:>30}, não é mesmo?'.format(K))
#Aqui, a seta > significa alinhamento à esquerda. Em 40 30 espaços ":30" a máscara
# "K" será jogada para os últimos espaços à esquerda. Com < isso é posto à direita
# e com ^ a máscara é alinhada em 30 espaços, conforme veremos a seguir.
L = input('Digite outra coisa')
print('Você digitou: {:^20}!'.format(L))
#Por fim, adicionaremos termos à máscara, os quais não estavam previamente inseridos
#usando-os como referência visual para o alinhamento.
H = input('Digite uma última coisa')
print('Você digitou: {:-^60}, pergunto-me o porquê...'.format(H))

#O código está funcional.





