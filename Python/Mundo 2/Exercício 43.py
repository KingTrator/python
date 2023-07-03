idade = int(input('Digite a idade do atleta: '))
if idade <= 9:
    print('MIRIM')
elif 14 >= idade > 9:
    print('INFANTIL')
elif 19 > idade > 14:
    print('JÚNIOR')
elif 20 >= idade >= 19:
    print('SÊNIOR')
else:
    print('MASTER')
