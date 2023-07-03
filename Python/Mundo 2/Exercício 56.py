# Criar um programa que leia o nome, idade e sexo de 4 pessoas.
# Ao fim, mostrar média das idades.
# Mostrar nome do homem mais velho, se houver.
# Mostrar quantas mulheres têm menos de 20 anos.
# O código funcionou até mostrar a média das idades, mas não consegui, adequadamente,
# reaizaro restanto das exigências. Abaixo, solução com ajuda integral do GPT-4.
'''d = 0
nomes = []
# Looping que lê nome, idade e sexo de 4 pessoas.
for i in range(2):
    name = input('Qual o seu nome? ')
    age = int(input('Qual a sua idade? '))
    sexo = input('Qual o seu sexo? ')
    d += age
    nomes.append(name.upper().strip())
    nomes.append(sexo.upper().strip())
    nomes.append(age)
# Média das idades.
print('A média das idades é {:.2f}'.format(d / 4))  # cuidado p/ definir o range certo
elemento = ''  # É importanter criar isto, pois caso elemento e idade não sejam completados com nenhum.
idade = 0  # valor ou string, o Python não dará erro, e retornará apenas uma lista vazia.
for i in range(0, len(nomes), 3):
    elemento = nomes[i + 1]
    if elemento == 'MASCULINO':
        idade = nomes[i + 2]

print(elemento)
print(idade)'''
# Código com ajuda do GPT-4
# Primeiro criaremos algumas variáveis para armazenar as informações.
# É importar este passo, pois caso uma das variáveis fique vazia, e esta é uma possibilidade,
# que deve ser aceita pelo Python, o script não dará um erro, mas retornará o valor inicial (nulo).
s_idades = 0  # Razão análoga a homem_velho_idade
homem_velho_nome = ''  # Como o homem será uma única string, não faz sentido usar lista []
homem_velho_idade = 0  # Como para idade precisamos adicionar números, usamos um int.
mulheres_novas = 0  # Razõa análoga a homem_velho_idade
for i in range(4):
    n = input('Digite seu nome: ').strip()
    a = int(input('Digite sua idade: '))
    g = input('Digite seu sexo (M/F): ').upper()
    s_idades += a
    if g == 'M' and a > homem_velho_idade:
            homem_velho_nome = n
            homem_velho_idade = a
    elif g == 'F' and a < 20:
            mulheres_novas += 1
print(f'A média das idades é {s_idades/4}')
print(f'O homem mais velho é o {homem_velho_nome}.')
print(f'{mulheres_novas} é o número de mulheres com menos de 20 anos.')


