from time import sleep
# import json Refaça, futuramente, o código usando esta biblioteca, fica bem mais simples.
# O exercício 115 é dividido em algumas partes.
# Aqui há um objetivo: criar um menu que:
# 1. Permita inserir novas entradas de usuário (nome e idade)   OK
# 2. Permita exibir as entradas inseridas em formatação tabular OK
# 3. Seja capaz de salvar as entradas dos usuários.             OK
# 4. Permita exibir o panorama de todas pessoas e respectivas idades adicionadas.   OK
# 5. Conte com a opção de sair do programa.
perma = list()
while True:
    print(f'\033[1;32m {"MENU DE OPÇÕES":>20}\033[m')
    ask = input('Para ver os usuários já adicionados, tecle 1\n'
                'Para adicionar novos usuários, tecle 2.\n'
                'Para fechar o programa, tecle 3\n=> ')
    if ask == '1':
        with open('ex115.txt', 'r') as f:
            temp = []
            print('-=' * 30)
            print(f'{"Nome":<20}', f'{"Idade":>20}')
            for linha in f:
                name, age = linha.strip().split(',')
                age = int(age)
                temp.append([name, age])
            for i, v in enumerate(temp):
                print(f'{v[0]:<20}{v[1]:>20}')
        print('-=' * 30)
        sleep(1)
        continue
    elif ask == '2':
        while True:
            while True:
                name = input('Nome do usuário: ').title().strip()
                tempname = name.replace(' ', '')
                if tempname.isalpha() is False:
                    print('Por favor, digite apenas letras para o nome de usuário. ')
                    continue
                else:
                    break
            while True:
                try:
                    age = int(input('Idade do usuário: '))
                except(ValueError, TypeError):
                    print('Por favor, digite uma idade válida.')
                else:
                    break
            perma.append([name, age])
            ask = input('Se quiser parar de adicionar, digite 3. Se não quiser, digite qualquer outra coisa: ')
            if ask == '3':
                break
        with open('ex115.txt', 'a') as f:
            for i in perma:
                f.write(f'{i[0]}, {i[1]}\n')
    elif ask == '3':
        break
    else:
        print('\033[1;31mERRO! Por favor, digite uma opção válida.\033[m')
print('VOLTE SEMPRE!')

