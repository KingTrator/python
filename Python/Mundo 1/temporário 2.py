import csv
from nltk import pos_tag
from collections import Counter

# Aqui eu simplesmente usei um código feito pelo ChatGPT para procurar um padrão
# em uma postagem de uma Projeto de Lei qualquer. O padrão é que tanto os críticos
# quanto aqueles que se mostravam favoráveis utilizavam vocabular muito próximo para
# adjetivar o projeto. Quer dizer, quem o achava ruim, dizia que ele era uma ameaça
# a liberdade. Quem o achava bom, dizia que ele era uma proteção a liberdade.
# E as pessoas eram honestas em suas afirmações contraditórias.

# Definir o caminho para o arquivo CSV
arquivo_csv = r'C:\Users\Win10\OneDrive\Desktop\PL.csv'

# Palavras a serem excluídas da análise
palavras_excluidas = [
    'um', 'uma', 'não', 'o', 'que', 'os', 'é', 'e', 'nos', 'nossa',
    'em', 'no', 'na', 'nas', 'para', 'por', 'com', 'sobre', 'sob',
    'entre', 'através', 'de', 'se', 'falar', 'ser', 'são', 'ou', 'qual',
    'esse', 'nosso', 'lei', 'dos', 'tal', 'ao', 'maior', 'nunca', 'leis',
    'atual', 'da', 'nem', 'total', 'nós', 'quem', 'notícias', 'controlar',
    'nada', 'opinião', 'inclusive', 'sua', 'empresas', 'news,', 'informações',
    'real', 'isso', 'regular', 'uso', 'penal', 'igual', 'querem', 'nome',
    'social', 'sem', 'usado', 'nossas', 'nesse', 'real', 'nada', 'controlar',
    'inclusive', 'sociais,', 'essa', 'empresas', 'suas', 'nesta', 'outra',
    'sociais.'
]

# Criar um dicionário para contar os adjetivos usados por quem é a favor ou contra o PL
adjetivos_favor = Counter()
adjetivos_contra = Counter()

# Dicionário para armazenar os comentários que mencionam as palavras-chave
contexto_palavras = {}

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

        # Realizar a análise gramatical das palavras e obter os adjetivos
        pos_tags = pos_tag(palavras)
        adjetivos = [
            palavra for palavra, pos in pos_tags
            if pos.startswith('JJ') and palavra.lower() not in palavras_excluidas
        ]

        # Contar os adjetivos usados por quem é a favor ou contra o PL
        if opiniao == 'positivo':
            adjetivos_favor.update(adjetivos)
        elif opiniao == 'negativo':
            adjetivos_contra.update(adjetivos)

        # Atualizar o contexto das palavras
        for palavra in adjetivos:
            if palavra not in contexto_palavras:
                contexto_palavras[palavra] = []
            contexto_palavras[palavra].append(conteudo)


# Obter os 4 adjetivos mais recorrentes por quem é a favor ou contra o PL
top_adjetivos_favor = adjetivos_favor.most_common(4)
top_adjetivos_contra = adjetivos_contra.most_common(4)

# Imprimir os adjetivos mais usados por quem é contra o PL
print("Adjetivos mais usados por quem é contra o PL:")
for adjetivo, frequencia in top_adjetivos_contra:
    print(f"Adjetivo: {adjetivo}, Frequência: {frequencia}")

# Imprimir os adjetivos mais usados por quem é a favor do PL
print("\nAdjetivos mais usados por quem é a favor do PL:")
for adjetivo, frequencia in top_adjetivos_favor:
    print(f"Adjetivo: {adjetivo}, Frequência: {frequencia}")
