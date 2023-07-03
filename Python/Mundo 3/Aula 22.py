import Aa       # Para o Python, todo arquivo.py é um módulo (em potencial).
# Observação: o python não recomenda, por exemplo, um from Aa import dobro, fatorial
# Isso porque, no caso de um script com importações múltiplas, pode ocorrer de uma biblioteca
# ter uma função de nome dobro ou fatorial também, o que gera conflito.
# Nesses casos, o que vale é sempre a última importação, o que pode não ser o desejado.
#  Estudo de modularizações.
# "Nessa aula, vamos continuar nossos estudos de funções em Python,
# aprendendo como criar módulos em Python e reutilizar nossos códigos em
# outros projetos. Vamos aprender também como agrupar vários módulos em um pacote,
# ampliando ainda mais a modularização em grandes projetos em Python."
# Direto a prática:
num = int(input('Número: '))
fat = Aa.fatorial(num)      # (Linha 1 a 5) daí o porque de usar Algumacoisa.Outracoisa
dob = Aa.dobro(num)
print(f'{num}! = {fat}')
print(f'O dobro de {num} = {dob}')

# Para o Python, toda pasta.py é um pacote em potencial. Se a pasta.py tiver outras pastas.py,
# cada uma delas será um pacote dentro do pacote maior que as contem. Já os arquivos, todos os arquivos.py
# são módulos importáveis. Pode-se importar a pasta maior como um todo, a subpasta dela ou seus módulos
# em específicos. Também é possível importar apenas a função específica dentro da pasta da subpasta com seu módulo
# que contem a função.
# NOTA! Se você estiver fora do Pycharm, para criar um módulo/pacote que funcione, você precisará de
# um __init__.py NECESSARIAMENTE para permiti-lo importar funções dele.
# CORREÇÃO! O GPT-4 disse-me que a partir da versão Python 3.4 isso não é mais necessário, mas que fique
# isso como nota.
# Ao criar um package (diretório/pasta/biblioteca) para um arquivo.py
# Não se deve usar espaço no nome da pasta, ou não será possível
# importá-la, também não use números ou adereços especiais.
# A convenção para nomenclatura é: números no começo dão erro,
# deve-se usar letras minúsculas
# espaços são interpretados com unidades distintas de código para o Python (não use)
# o único adereço especial válido é __
# Exercícios do 107 ao 112.