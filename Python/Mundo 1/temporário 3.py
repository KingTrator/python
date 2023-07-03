# Ainda não cheguei nessa parte do Python, mas estava curioso quanto
# ao tratamento de erros. Digite uma letra  para obter resposta de erro.
try:
    name = int(input('Digite um número: '))
    print('O número digitado é {}.'.format(name))
except Exception as e:
    print('Ocorreu um erro ao processar o nome que você digitou.')
    print('Certifique-se de que está digitando apenas caracteres alfabéticos, sem espaços extras no início ou no fim.')
    print('Detalhes do erro:', e)

# Depois de quase duas semanas, cheguei na parte de tratamento de erros.