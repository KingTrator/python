demaior = 2005
nome_maior = []
q1 = 0
nome_menor = []
q2 = 0
for i in range(7):
    age = int(input('Digite seu ano de nascimento: '))
    name = input('Qual é o seu nome? ')
    if age <= demaior:
        nome_maior.append(name)  # Usa-se append para adicionar termos como uma lista às listas.
        q1 += 1
    else:
        nome_menor.append(name)  # E usa-se extend para adicionar itens um a um às listas ou tuplas.
        q2 += 1
#if q1 > 0 and q2 > 0:
#    print(f'São {nome_maior} aqueles que já são (ou serão neste ano) maiores de idade.')
#    print(f'São {nome_menor} aqueles que ainda não são maiores de idade.')
#elif q1 == 0 and q2 > 0:
#    print(f'{nome_menor} são todos menores de idade.')
#else:
#    print(f'{nome_maior} são todos maiores de idade (ou serão neste ano).')
# É possível tornar esta última parte do código mais legível, ao usar a função
# 'algumacoisa'.join(outracoisa), pois a função join toma uma lista ou quaisquer
# sequências de strings e
if q1 > 0 and q2 > 0:
    print(f'São {", ".join(nome_maior)}, aqueles que já são (ou serão neste ano) maiores de idade.')
    print(f'São {", ".join(nome_menor)}, aqueles que ainda não são maiores de idade.')
elif q1 == 0 and q2 > 0:
    print(f'{", ".join(nome_menor)}, são todos menores de idade.')
else:
    print(f'{", ".join(nome_maior)}, são todos maiores de idade (ou serão neste ano).')
