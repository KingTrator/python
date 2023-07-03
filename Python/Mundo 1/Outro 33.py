from datetime import date
a = int(input('Digite o ano que você deseja descobrir se é ou não bissexto: '))
if a == 0:
    a = date.today().year
if (a % 4 == 0 and a % 100 != 0) or (a % 400 == 0):
    print('{} É bissexto.'.format(a))
else:
    print('{} Não é bissexto.'.format(a))
# !=
# ''' a1 = str(a)
# a2 = [a1]
# if len(a2) == 0 or len(a2) == 1:
#     a % 4
# if a % 4 == 0:
#     print('{} é ano bissexto.'.format(a))
# if len(a2) == 2:
#     a % 400
# if a % 400 == 0:
#         print('{} é ano bissexto'.format(a))
# if a % 4 or
#     print('{} não é ano bissexto.'.format(a))
# # O código está funcional.
