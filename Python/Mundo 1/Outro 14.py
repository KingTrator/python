import random
print('\033[1;31m', random.random(), '\033[m')
# A classe random zera um número aleatório entre 0 e 1.
# Você pode pedir para que ele execute números inteiros também.
# Isso apenas multiplica o resultado por três em vez de
# fazê-lo aparecer três vezes.
print('\033[1;31m', (random.randint(1, 10))*3, '\033[m')
num = random.randint(1, 5)
SSS = str(num) + '||'
print('\033[1;31m', SSS * 3, '\033[m')
#Por meio de uma simples modificação, cria-se uma variável chamada num, a qual
# pertence à classe int. Na sequência, modifica-se a classe para str dentro de outra função (SSS), assim
# é possível clonar as respostas por um valor inteiro qualquer. Para que
# 2, por exemplo, não apareça como 22222... adiciona-se um espaço '||' com duas
# barrinhas apenas para separá-los.

# Nota: evite dar o nome de variáveis coincidentemente com o de classes.
# Eu havia chamado SSS, anteriormente, de str.

















