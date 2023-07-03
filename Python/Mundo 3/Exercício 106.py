# Exercício Python 106: Faça um mini-sistema que utilize o
# Interactive Help do Python. O usuário vai digitar o comando e o manual vai aparecer.
# Quando o usuário digitar a palavra ‘FIM’, o programa se encerrará. Importante: use cores.


def ajudante(msg):
    c = 0
    if msg == '':
        while True:
            a = input(f'\033[1;4{c}mOlá! No que posso lhe ajudar? ')
            help(a)
            ask = input('Gostaria de sair? (FIM para sair) ').strip().upper()
            if ask == 'FIM':
                print('\033[m\033[1;32m PROGRAMA FINALIZADO!\033[m')
                break
            c += 2
            if c == 6:
                c = 0
    else:
        print('Ok, você realizou um teste. Na próxima, coloque apenas aspas simples nos parenteses.\033[1;44m')
        help(msg)


ajudante('')