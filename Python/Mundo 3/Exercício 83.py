# Exercício Python 083: Crie um programa onde o usuário digite uma
# expressão qualquer que use parênteses. Seu aplicativo deverá analisar se a
# expressão passada está com os parênteses abertos e fechados na ordem correta.
# Obs: o exercício, como escrito, é muito complexo, então eu vou
# me limitar a analisar a igualdades de pabertas e pfechado, como uma
# solução mais trivial.
expressao = input('Digite uma expressão matemática: ').strip().replace(' ', '')
pilha = []
for char in expressao:
    if char == '(':
        pilha.append('(')
    elif char == ')':
        if len(pilha) > 0:
            pilha.pop()
        else:
            pilha.append(')')
            break
if len(pilha) == 0:
    print('Sua expressão está válida!')
else:
    print('Sua expressão está errada!')
