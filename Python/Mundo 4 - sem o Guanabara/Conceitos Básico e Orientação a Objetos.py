# A ordem provável do CeV para o curso de Python seria o estudo sobre classes em Python.
# No entanto, não é essa a ordem que o curso de Python no Coursera (que estou fazendo) realizado por um professor
# da universidade de Michigan segue. Antes de POO vê-se o módulo re em Python.
# No entanto, devido a necessidades atuais, preciso estudar um pouco sobre POO em Python para depois seguir
# a ordem do curso no Coursera.
# O que segue abaixo é uma mescla de aprendizados de diferentes professores, em especial o do canal
# "Hashtag Programação".

# Classe > Objeto > Atributo.
# Objetos modificam seus Atributos por meio de Métodos.

class Pessoa:  # Pessoa é o geral, "Roberto" é o particular.
    def __init__(self, nome, idade):
        self.nome = nome  # Atributo de pessoa.
        self.idade = idade # Atributo de pessoa
        # Toda pessoa, como "Roberto", tem atributos.
        # Mas os particulares de "Pessoa" não são iguais.
        # Os métodos modificam os atributos da "Pessoa" em particular
        # Também podem fazer a "Pessoa" em particular realizar ações, como abaixo:

    def falar(self):  # Uma pessoa pode possuir o método "falar", ou seja, método pode ser uma ação.
        print(f'Olá, meu nome é {self.nome} e tenho {self.idade} anos.')
        # Mas também pode haver um método para alterar a idade, por exemplo.
p = Pessoa('Pedro', 23) # Instanciando o objeto
p.falar() # Chamando o método da classe "Pessoa"

# Seguindo __________________________________________

class ControleRemoto:
    def __init__(self, cor, altura, profundidade, largura):  # Os atributos (características) devem estar dentro desta
        # função padronizada.

        self.cor = cor   # Usa-se "self." antes da variável para indiciar ao Python que a variável em questão é um atri
        self.altura = altura  # buto da classe.
        self.profundidade = profundidade  # Além disso, diz-se, por exemplo, "self.cor" = cor para que a "cor" possa ser
        self.largura = largura  # definida pelo programador a posteriori, em vez de ser algo fixo, como "preto".
        # Só para constar, não é preciso que a característica tenha o mesmo nome do valor que ela recebe.
        # Eu poderia ter feito self.cor = a sem nenhum problema (desde que em cima trocasse "self, cor" por "self, a"
        # No caso, "a" seria a variável da característica "cor". Por isso é coerente dizer que a característica "cor"
        # tem uma variável chamada "cor", que é quem recebe os valores dos atributos.

        # Aqui não entram os métodos, como "ligar TV", pois isso é algo que o controle pode fazer e não necessariamente
        # um atributo - mas como dito, os métodos também podem modificar atributos.
        # Nota: self é, ainda mais especificamente, a função de início, aquela que é relativa aos atributos iniciais.


        # Toda função que tem "__init__" em uma Classe pode ser recuperada depois e ter seus atributos alterados.


    def passar_canal(self, botao=''):
        if botao == '+':
            print('Aumentar o canal')
        elif botao == '-':
            print('Diminuir o canal')
        # métodos do controle remoto:
        #   - trocar o canal
        #   - alterar o volume
        #   - abrir a Netflix
        #   - desligar a TV


# Instâncias da Classe "ControleRemoto()":
controle_remoto1 = ControleRemoto('preto', '10cm', '2cm', '2cm')

controle_remoto2 = ControleRemoto('azul', '5cm', '1cm', '1cm')
# OBS: _______________
# As instâncias são os objetos que são criados por uma Classe.
# IMPORTANTE: Todo objeto é uma instância de uma classe, mas uma instância não é necessariamente um objeto.
# Instância sempre remete a alguma classe. A razão para os termos não serem coincidentes remete a outros assuntos que
# ainda não estudei e não é necessário saber no momento (talvez nem no futuro).
# Por enquanto, não há problemas em intercambiar "instância" e "objeto", pois, neste contexto, são símiles.
# ___________________
# Como dito no exemplo acima, "self.cor = cor" permite definir os atributos do particular da classe dentro do código.
# Aqu vê-se isso acontecer:
print(controle_remoto1.cor)  # a cor do controle remoto será exibida
# Se você remover "self." de qualquer atributo, o Python retornará o erro: "AttributeError: "ControleRemoto" object has
# no attribute 'cor'. Ou seja, o "self." é como eu digo ao Python: "Ei, Python! Isso aqui é uma característica da minha
# "Classe, ok?". Sem isso, é como se eu tivesse soltado um "Barbar" ao Python - referência aos bárbaros da Roma Antiga.
# Não é bem isso claro, o Python ainda reconhece "cor" como uma variável.

controle_remoto1.passar_canal('+')

# Diferenças semânticas entre métodos e atributos:
# O atributo não possui um "()" ele é chamado por meio de "objeto.atributo", isto é, tem o formato ".atributo".
# O método, por outro lado, é chamado por um "()", seria "objeto.método()", isto é, tem o formato ".método()".
# OBS: Neste contexto, método == função (que não a __init__).

# Para finalizar, vamos a um exemplo prático, criando uma classe para clientes da Netflix.



class Cliente:
    def __init__(self, nome, email, plano): # Aqui devemos criar todas as variáveis da classe.
        self.nome = nome
        self.email = email
        # E se o cliennte colocar um plano inválido (considerando-se isso possível de alguma forma)?
        # Podemos realizar um pequeno tratamento de erros, limitando os planos:
        self.lista_planos = ['básico', 'premium'] # Essa variável poderá ser chamada por outras funções desta classe.
        # Ainda assim, "self.lista_planos" não pode ser invocada fora da classe, pois não foi dada como parâmetro de
        # def __init__
        # lista_planos (sem self.) = essa variável só existe nesta função e não pode ser invocada fora daqui.
        if plano in self.lista_planos:
            self.plano = plano # Se o plano escolhido estiver na lista supracitada, ele recebe o valor
            # Se não...
        else:
            raise Exception('Plano Inválido')
            # ... levanta-se a exceção "Plano Inválido".

    # Se você manter apenas "lista_planos" como está na função __init__, há um problema, porque ela está como um
    # escopo local e não global. No entanto,
    def mudar_plano(self, novo_plano):
        if novo_plano in self.lista_planos:
            self.plano = novo_plano
        else:
            print('Plano inválido')
            # raise Exception('Plano Inválido')
            # para continuar o código, vou deixar o raise Exception, mais preciso, como comentário.

    def ver_filme(self, filme, plano_filme):
        if self.plano == plano_filme:
            print(f'Ver filme {filme}')
        elif self.plano == 'premium':
            print(f'Ver filme {filme}')
        elif self.plano == 'basico' and plano_filme == 'premium':
            print('Faça o upgrade para ver este filme')
        else:
            print('Plano Inválido')
# Imagine que dentro do site, que é front-end, o cliente clica em um botão para se registrar como um cliente.
# A ideia é que no back-end essa função seja chamada para efetivamente gerar os dados de um cliente.

cliente = Cliente('Lira', 'exemplo@exemplar.com', 'premium')
cliente.mudar_plano('básico') # Troquei o plano de "premium" para 'básico'
print(cliente.plano)  # Verifica-se que a troca foi bem sucedida.
# Além disso, o cliente será adicionado a algum banco de dados.
# Não é o caso deste código, mas o que se seguiria no back-end seria algo como:
# "cliente.add_to_database"

cliente.ver_filme('Harry Potter e Afonso', 'premium')
# Aqui você receberá um "Plano Inválido", pois self.plano, após o "cliente.mudar_plano = 'básico', está definido como
# "básico"
# No entanto, ao mudar isso, será possível assistir Harry Potter e Afonso.
cliente.mudar_plano('premium')
cliente.ver_filme('Harry Potter e Afonso', 'premium')