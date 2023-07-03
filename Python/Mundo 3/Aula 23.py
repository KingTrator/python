# Tratamento de Erros e Exceções
# "Nessa aula, vamos ver como o Python permite tratar erros e criar respostas a essas exceções.
# Aprenda como usar a estrutura try except no Python de uma forma simples."
# n = int(input('Número: '))
# print(n)    # mas use n = str
# ValueError: invalid literal for int() with base 10: 'olá'
#  Vamos tratar dessa EXCEÇÃO.
#a = int(input('Num: '))
# b = int(input('Num: '))  # escolha b = 0.
# r = a / b
# print(r)    # ZeroDivisionError: division by zero
# print(2/'2') # TypeError
# lst = [3, 6, 4]
# print(lst[3])     # IndexError / nos dicionários, KeyError.
# import cudecachorro   # ModuleNotFoundError
# Essas são apenas algumas das exceções
# É aqui que entra try e except.
# Até então, eu dava ordens quanto aquilo que deveria ser executado pelo Python.
# Com try, eu peço para que ele faça algo, se for possível.
# Se não for possível, caímos no except.
try:
    a = int(input('Digite um número: '))
    b = int(input('Digite um número: '))
    r = a /b

except:     # O problema aqui é que eu estou tratando qualquer erro, o Pycharm prefere que eu o especifique.
    print('\033[1;31mERRO! Digite apenas números inteiros, não digite letras nem divida por 0\033[m')

else:
    print(r)    # print(r) só acontece se try for possível, mas colocar um else aqui garante
                # não exibir um NameError ou um Erro de divisão por 0, mas somente o "Except".
finally:        # É executado se independemente de ter dado "try" ou "except", enquanto "else" só rola para "try".
    print('Volte sempre!')

# Melhorando o código anterior:
try:
    a = int(input('Digite um número: '))
    b = int(input('Digite um número: '))
    r = a / b
except Exception as erro:
    print(f'Problema encontrado! Foi {erro.__class__}')
else:
    print(r)
finally:
    print('Volte sempre!')

# NOTA IMPORTANTE: NUNCA MOSTRE AO USUÁRIO O MOTIVO DA EXCEÇÃO! Isso pode causar erros de segurnaça
# e tornar o programa mais suscetível a ATAQUES HACKERS. Use apenas uma mensagem genérica para isso.
# A única razão para expor uma Exception é para que você mesmo teste seu programa.
# Para analisar erros durante o programa, você pode importar o módulo logging para registrá-los
# a parte e verificá-los depois.
# Também é possível, para um único "try", colocar em cascata os exception:
try:
    a = int(input('Digite um número: '))
    b = int(input('Digite outro número: '))
    r = a / b
except ValueError:
    print('\033[1;31mERRO! Digite apenas números inteiros.\033[m')
except ZeroDivisionError:
    print('\033[1;31mERRO! Não é possível dividir por zero.\033[m')
else:
    print(r)
