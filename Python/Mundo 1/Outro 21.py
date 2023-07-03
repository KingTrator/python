frase = ('LOKA')
print(frase[0:4])
# A frase será completamente lida se expressarmos 0:4. Se expressarmos 0:3,
# O último A não irá aparecer.
print(frase[0:3])
# Isso ocorre porque o último caracter não é contado. Nesta versão, o problema parece
# ter sido corrigido em relação ao curso de Python que estou vendo. Isso porque
# como o primeiro índice = 0, o último irá coincider com a última letra da frase.
# Portanto, basta lembrar que, para o python I0 = primeira leitra, I1 = segunda letra
# e segue.

pica = ('O rato roeu a roupa do rei de Roma')
print(pica[:5])
#Neste caso, 5 é o caracter de limite para receber o print. Ou seja, ler-se-á
# tudo que for de 0 até 5, sem contar o 5, sendo I5 = o.
# Por outro lado...
print(pica[5:])
#Aqui a frase se inicia I5 = o e termina no último caracter.
print(pica[5:10])
#Já neste caso, incia-se em I5 e termina-se antes de I10.
print(pica[3::2])
#Além disos, pode-se definir o início como I3 até o fim da frase (poderia ter
# definido um caracter para parar, como, por exemplo, 3:10:20). Na sequência,
# :2 pede para que o programa pule duas letras, a partir de I3 (que será lido)
# contando o último caracter do pulo. Isto é, para :2, uma letra é comida por vez.
# Caso você tenha um frase grande e deseje saber quantos caracteres há em uma frase,
# pode-se usar o len.
K = ('EFHFJH ERF H8743 RHFEUFG4 HSB F348 FY34F Y7494HRFW FSJKDFDDSHB JFF 344F9'
     ' RUIHF RIUEF HREGF 538749F G834 GF37498J FG3Y4F ')
print(len(K))

