import csv
from collections import Counter

# Este código foi feito totalmente pelo GPT-3.5. Vou deixá-lo aqui apenas porque
# achei interessante a função Counter, mas pretendo apagar isto com o tempo.
# Definir o caminho para o arquivo CSV
arquivo_csv = r'C:\Users\Win10\OneDrive\Desktop\PL.csv'

# No final do mundo 3 eu fiz um exercício bastante parecido com esse. Fiquei de
# criar uma versão alternativa dele, usando json.

# Criar um dicionário para contar as palavras usadas por quem é a favor ou contra o PL
palavras_favor = Counter()
palavras_contra = Counter()

# Abrir o arquivo CSV
with open(arquivo_csv, 'r', newline='', encoding='utf-8') as arquivo:
    leitor = csv.reader(arquivo)
    # Ignorar a primeira linha (título)
    next(leitor)

    # Ler cada linha do arquivo
    for linha in leitor:
        # Obter a opinião registrada (positivo ou negativo)
        opiniao = linha[0].lower()

        # Obter o conteúdo da opinião (restante da linha)
        conteudo = ' '.join(linha[1:])

        # Dividir o conteúdo em palavras
        palavras = conteudo.split()

        # Contar as palavras usadas por quem é a favor ou contra o PL
        if opiniao == 'positivo':
            palavras_favor.update(palavras)
        elif opiniao == 'negativo':
            palavras_contra.update(palavras)

# Obter as 4 palavras mais recorrentes por quem é a favor ou contra o PL
top_palavras_favor = palavras_favor.most_common(4)
top_palavras_contra = palavras_contra.most_common(4)

# Imprimir as palavras mais usadas por quem rejeita o PL
print("Palavras mais usadas por quem é contra o PL:")
for palavra, frequencia in top_palavras_contra:
    print(f"Palavra: {palavra}, Frequência: {frequencia}")

# Imprimir as palavras mais usadas por quem é a favor do PL
print("\nPalavras mais usadas por quem é a favor do PL:")
for palavra, frequencia in top_palavras_favor:
    print(f"Palavra: {palavra}, Frequência: {frequencia}")
