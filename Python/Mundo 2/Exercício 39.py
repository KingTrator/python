from datetime import datetime

print('\033[1;33mALISTAMENTO OBRIGATÓRIO\033[m')
a = int(input('Digite o ano em que você nasceu: '))
I1 = datetime.now().year - a
if I1 == 18:
    print('Você tem (ou fará neste ano) {} anos, portanto deverá se alistar este ano.'.format(I1))
elif I1 >= 19:
    print('Você tem (ou fará neste ano) {} e deveria ter se alistado há {} anos.'.format(I1, (I1 - 18)))
else:
    print('Você tem (ou fará neste ano) {}, portanto deverá se alistar daqui a {} anos.'.format(I1, ((-1)*(I1 - 18))))
