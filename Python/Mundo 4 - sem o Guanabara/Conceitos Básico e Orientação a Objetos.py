# Eu parei um pouco com POO para estudar pela ordem do curso que se baseia
# no livro "Python para todos", o qual está no Coursera. Pela ordem, agora eu estudo mais sobre
# o pode do Python de modificar arquivos e fazer leituras voltadas à Ciência de Dados.
# POO é o próximo capítulo. Ainda assim, fica aqui o início de POO em Python:

# Infelizmente, o mundo 4 de Python do CeV ainda não está disponível, mas eu preciso continuar meus
# estudos em programação. Por isso, estou iniciando um curso de POO pelo Coursera, ministrado por um
# professor, aparentemente, que estudou na USP e IME.
# A POO seria o próximo passo natural do CeV, então faz sentido continuar meus estudos com ela.
# Objeto --> Encapsula dados(variáveis, atributos) ou códigos(funções, métodos)
# Classe --> É uma "receita" que define ~;os elementos presentes em um cojunto de objetos, descrevendo
# os métodos, atributos, dando nomes ou tipos (type) das variáveis, parâmetros, etc.
# A classe também pode criar objetos
# Para definer uma classe em Python, basta fazer:
class Pessoa:
    def __init__(self, nome, idade):
        self.nome = nome
        self.idade = idade


    def falar(self):
        print(f'Olá, meu nome é {self.nome} e tenho {self.idade} anos.')

p = Pessoa('Pedro', 23) # Instanciando o objeto
p.falar() # Chamando o método da classe "Pessoa"
