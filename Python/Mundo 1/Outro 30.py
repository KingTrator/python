A = float(input('Digite o número em Km/h, e apenas o número, da velocidade do carro: '))
if A > 80:
    B = int(A)
if A <= 80:
    print('Está tudo bem, você está dentro da velocidade limite.')
else:
    print('Você passou do limite de 80Km/h, pois está a {}Km/h'.format(A))
    print('Isso quer dizer que você terá de pagar uma multa.')
    print('A multa é de R$7.00 por cada Km extra.')
    print('Com efeito, sua multa final é de {}x7, sem considerar os decimais.'.format(B - 80))
    print('Valor total a pagar: R${}.'.format(int(B - 80)* 7))

# O código está funcional. No entanto, é possível simplificá-lo, conforme o GPT-4:
A = float(input('Digite o número em Km/h, e apenas o número, da velocidade do carro: '))

if A > 80:
    B = int(A)
    excesso = B - 80
    multa = excesso * 7

    print('Você passou do limite de 80Km/h, pois está a {}Km/h'.format(A))
    print('Isso quer dizer que você terá de pagar uma multa.')
    print('A multa é de R$7.00 por cada Km extra.')
    print('Com efeito, sua multa final é de {}x7, sem considerar os decimais.'.format(excesso))
    print('Valor total a pagar: R${}.'.format(multa))

else:
    print('Está tudo bem, você está dentro da velocidade limite.')
