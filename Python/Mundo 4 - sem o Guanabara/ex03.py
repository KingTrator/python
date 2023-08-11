import socket

mysock = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
mysock.connect(('data.pr4e.org', 80))
cmd = 'GET /romeo.txt HTTP/1.0\r\nHost: data.pr4e.org\r\n\r\n'.encode()  # codifica a string em bytes para enviá-la.
mysock.send(cmd)

while True:
    data = mysock.recv(512)  # carrega até 512 bytes da página
    if len(data) < 1:        # Se menos de 1byte (ou seja, nada, pois esse é o mínimo) for retornado, quebra o looping.
        break
    print(data.decode())     # Decodifica os bytes enviados pelo servidor.
mysock.close()

# Resultados:
"""HTTP/1.1 200 OK ---> Solicitação bem sucedida (200 == OK), versão do protocolo HTTP é 1.1
Date: Fri, 11 Aug 2023 17:01:51 GMT ---> Data e hora do envio da resposta
Server: Apache/2.4.18 (Ubuntu) ---> 
Last-Modified: Sat, 13 May 2017 11:22:22 GMT  ---> Exatamente isto: última modificação do arquivo.
ETag: "a7-54f6609245537"
Accept-Ranges: bytes  
Content-Length: 167 ---> Tamanho do corpo da resposta (167 bytes)
Cache-Control: max-age=0, no-cache, no-store, must-revalidate
Pragma: no-cache
Expires: Wed, 11 Jan 1984 05:00:00 GMT  
Connection: close  ---> Controla a conexão após realizado o envio dos pacotes solicitados. Neste caso, fecha.
Content-Type: text/plain  ---> Define o tipo de conteúdo que foi enviado

Aqui está um pequeno poema de Shakespeare.
"""
# Definição de SOFTWARE: Conjunto de instruções e dados que o computador pode usar para realizar tarefas.
# É a parte não tangível do computador. Permite controlar o Hardware (parte tangível) diretamente.
# Há tipos como, software operacional (Windows, Linux...), de aplicação (Chrome, Firefox, processadores de texto),
# de programação(IDEs como o PyCharm, compiladores)....
# APACHE é um software de servidor web. Um servidor é o computador "central" por meio do qual a informação circula.
# Pela internet, via de regra, esses servidores estão localizados nos grandes data centers. No caso do Apache, ele é um
# software de distribuição gratuita que controla o fluxo da informação de algum outro servidor.
# UBUNTU: é um sistema operacional de dispositivos Linux.

# TODAS AS PROPRIEDADES ABAIXO SÃO DEFINIDAS PELO SERVIDOR BACK-END:

# ETAG: é um tipo de CPF do conteúdo que foi solicitado por meio do soquete. Após acessá-lo uma primeira vez e obter a
# ETag, nas próximas vezes você poderá apenas verificar se a ETag foi modificada. Se sim, significa que o conteúdo
# solicitado (a cópia que temos) sofreu modificações e você pode querer baixá-lo novamente.
# Há outros usos, como um meio do servidor evitar a sobreposição de modificações - se dois usuários modificarem o
# conteúdo para uma mesma ETag, uma iria se sobrepor a outra, ou seja, a mais recente em relação a última. Mas
# a última recebe uma nova ETag, logo, a próxima modificação, que usa uma ETag anterior, não surtirá efeito, o que evita
# sobreposição.
# Também é útil para conferir se os dados que foram transferidos pelo servidor foram corrompidos durante o processo.
# Se os dados não foram alterados, você receberá "303 Not Modified".

# Accept-Ranges: Indica se o servidor aceita ou não solicitações de intervalo.
# Solicitações de intervalo, basicamente, são solicitações feitas com base em arquivos de desejo e na quantidade
# de dados que se quer baixar. Neste caso, aceita-se bytes, portanto, podemos definir o número de bytes que queremos
# extrair através do soquete. Se o valor fosse "none", então não seria possível delimitar um intervalo, mas sim apenas
# extrair todo o conteúdo através do soquete.

# Content-Length: Tamanho do conteúdo extraído. (167 bytes)

# Cache-Control: Diz como se dá o controle do cache para o cliente. Neste caso, no qual estou fazendo uma transmissão
# direta através do soquete, esse dado não é tão importante, porque não vou armazenar cache de qualquer forma, é uma
# informação útil para navegadores. Aqui está definido para não armazenar cache.

# Pragma: Similar ao Cache-Control, é mais antiga e é usada para dar compatibilidade com versões antigas do HTTP.

# Connection: define se a conexão é mantida após a transação atual. Neste caso, diz-se para fechá-la.
# Eu também reforço isso com socket.close() ao final do código.

# Content-type: define o tipo de conteúdo em questão.
