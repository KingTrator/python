preco = float(input('Digite o preço do produto: '))
opcao = int(input('Pressione 1 para pagamento à vista no cheque, boleto ou PIX (10% de desconto)'
                  '\n pressione 2 para pagamento à vista no cartão (5% de desconto)'
                  '\n pressione 3 para pagamento em até 2x no cartão (sem juros)'
                  '\n pressione 4 para pagamento em 3x ou mais no cartão (incorre em juro): '))
if opcao == 1:
    print('O preço final com o desconto é R${:.2f}.'.format(0.9 * preco))
elif opcao == 2:
    print('O preço final com o desconto é R${:.2f}.'.format(0.95 * preco))
elif opcao == 3:
    print('O preço final com o desconto é duas vezes de R${:.2f}, total: R${:.2f100}.'.format(preco/2, preco))
elif opcao == 4:
    n = int(input('Em quantas parcelas você irá pagar? '))
    juros = (preco * ((1 + 0.02) ** n))
    print('Você irá pagar em cada uma das {} parcelas R${:.2f}, ao todo: {:.2f}'.format(n, juros/n, juros))
