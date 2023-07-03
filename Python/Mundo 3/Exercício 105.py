# Exercício Python 105: Faça um programa que tenha uma
# função notas() que pode receber várias notas de alunos e vai retornar
# um dicionário com as seguintes informações:
# – Quantidade de notas OK
# – A maior nota  OK
# – A menor nota  OK
# – A média da turma  OK
# – A situação (opcional)


def notas(*msg, sit=False):
    '''

    :param msg: variadas notas que podem ser adicionadas
    :param sit: Opcional, se True, indica se a situação é OK ou Ruim
    :return: Dicionário com maior nota, menor nota, média, situação(se sit=True) e total de notas.
    '''
    maior_nota = menor_nota = soma_notas = 0
    for i in range(len(msg)):
        soma_notas += msg[i]
        if i == 0:
            maior_nota = menor_nota = msg[i]
        else:
            if maior_nota < msg[i]:
                maior_nota = msg[i]
            if menor_nota > msg[i]:
                menor_nota = msg[i]
    dicionario = {'Total:': len(msg), 'Maior nota:': maior_nota, 'Menor nota:': menor_nota,
                  'Média:': f'{(soma_notas/len(msg)):.2f}'}
    if sit is False:
        return dicionario
    else:
        if (soma_notas/len(msg)) > 7:
            dicionario['Situação'] = 'OK'
        else:
            dicionario['Situação'] = 'Ruim'
        return dicionario


print(notas(9, 7.5, 8))
