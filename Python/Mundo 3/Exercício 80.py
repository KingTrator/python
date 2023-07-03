# O programa deve ler 5 valores inteiros.
# Os valores devem ser colocados em uma lista.
# A lista deverá ser ordenada, mas não por meio da função sort().
lista = []
pos = 0
for i in range(5):
    num = int(input('Digite um número: '))
    if i == 0 or num > lista[-1]:  # Para o primeiro valor ou se num é maior que o último.
        lista.append(num)
    else:
        while pos < len(lista):
            if num <= lista[pos]:
                lista.insert(pos, num)
                break
            pos += 1
print(lista)
# Apesar de ter errado nas minhas várias tentativas, fico feliz
# pela solução, que é bem elegante e curta.