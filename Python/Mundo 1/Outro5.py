n = input('Digite qualquer bosta')
print('Verificação das características do input em relação a'\
       '\nser ou não alfabético, ser ou não numérico e a qual'\
       '\nclasse pertence o input.',\
       '\nO input é alfabético?', str(n.isalpha()),\
       '\nO input é numérico?', str(n.isnumeric()),\
       '\nQual a classe do input?', str(type(n)))

#Parabéns! Você executou o código de uma maneira muito mais sofisticada do que a
#aquela que havia sido proposta pelo professor. Então, aprendi duas novas formas
#de trabalhar por aqui "\" e "\n". Legal. No entanto, teria sido mais simples apenas
#dar vários prints em sequência. Aí sim você poderia ter mandado um "n.isalpha() e
# isso não demanria um str(n.isalpha()). Enfim, é isso. Os comentários abaixo
#seguem antes de eu ter feito a verificação da resolução do exercício proposto.

#O código está operante e funcional. Tive vários problemas para executá-lo e precise
# da ajuda do chatGPT para completá-lo corretamente. Primeiramente, eu não sabia como
#realizar uma quebra de linha aqui dentro do interpretador. Aprendi que a barra invertida
# "\" realiza essa função, escreva-a e aperte enter, isso fará com que o código seja
# quebrado do mesmo modo que fiz acima. Além disso, não queria que a frase aparecesse
# muito longa no interpretador. Então precise usar o comando \n para que também houvesse
# quebra no interpretador quando o código estivesse ativo (quebrar aqui e quebrar
# com o código ativo são coisas distintas... obviamente não estou usando as palavras
#mais precisas para descrever a situação-problema.
#Além disso, tive vários outros problemas menores. Em parte, por própria ação do Pycharm,
#que tentou me ajudar atrapalhou. Esqueci de colocar vírgulas entre os ARGUMENTOS,
#pois foi fácil esquecê-las ao realizar as quebras "\", ficava parecendo não ser necessário.
#Outrossim, não sabia usar os comandos "isalpha" e similares direito. Aparentemente,
#para usá-los em uma sntença como fiz, é preciso adicionar a classe "str" antes.
m = input('Digite algo')
print(m.isalpha())
#Mas neste exemplo (line 25) não foi preciso. Não sei... Talvez dê para fazer
# dos dois jeitos? Estou cansado demais para testar. Ou talvez seja algo específico
#para aquele código longo. Enfim, estou aprendendo.


