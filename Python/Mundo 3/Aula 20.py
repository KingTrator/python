# Estudo sobre Funções em Python.
# Funções são usadas para definir ROTINAS, isto é, coisas que se faz habitualmente
# nos próprios programas e, para facilitá-los, podemos definir (def) uma função
# para agilizar o processo.
# Exemplo, uso print('-=-=-=-=-=-=-=-=-=-=-=-=-=') com muita frequência. Posso
# definir isso uma única vez e depois usar a função neste e em outros scripts meus.
def mostralinha():
    print('-='*30)


mostralinha()   # Entre o def e o programa principal, o PEP clama que se use duas linhas em brancos
print('Olá, mundo!')    # mas isso apenas para fins estéticos.
mostralinha()
print('Este já não é mais meu primeiro programa em Python!')
mostralinha()
print('A jornada foi longa, mas estou aqui!')
mostralinha()
print('E isso, meu leitor, é uma grande vitória!')
mostralinha()
# Mas é possível ser mais eficiente. O padrão mostralinha() print pode ser usado a meu favor.


def mensagem(msg):  # msg é um parâmetro
    print('-='*30)
    print('\033[1;33m', msg,'\033[m')   # clique em "msg". Note que em mensagem(msg) acenderá uma "luz"
    print('-='*30)                      # esse é o sentido do parâmetro, marca onde está o conteúdo de ().


mensagem('Olá, de novo, mundo!')
mensagem('Este é mais um exemplo de como funções facilitam a vida.')
mensagem('A programação se baseia em coisas simples dando soluções complexas :)')

# <-- Outros exemplos. Abaixo, eu "escondi" o código, o que é útil. Faça isso ao clicar nos números ao lado <----


def soma(a, b):
    s = a + b
    print(f'{a} + {b} = ', s)


soma(3, 5)
mostralinha()
soma(b=4, a=9)  # Posso trocar a ordem deste modo.
mostralinha()
soma(100, 2240)     # Este código ainda está relativamente estático, vamos melhorá-lo...

def contador(*num):         # O símbolo * é um "desempacotador". Ele quer dizer que vários valores serão passados
    tam = len(num)
    print(f'Recebi os valores {num}, que são ao todo {tam} números.')   # e todos eles serão colocados em um "num"

contador(1, 2, 3, 4, 5)
contador(934, 3243, 4234)


def dobra(lst):       # Neste caso, farei listas, que já são variáveis compostas, por isso não preciso de *
    pos = 0
    while pos < len(lst):
        lst[pos] *= 2
        pos += 1


lista = [10, 20, 30, 100, 500, 65]
print(lista)
dobra(lista)
print(lista)


def soma(*valores):
    s = 0
    for n in valores:
        s += n
    print(f'Somando os valore {valores} = {s}')


soma(1, 2, 3)
soma(0, 0, 0)
soma(10, 10, 10)
soma(20, 30, 50)


# Exercícios do 96 ao 100.