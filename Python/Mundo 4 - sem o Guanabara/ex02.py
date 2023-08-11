import socket
mysock = socket.socket(socket.AF_INTET, socket.SOCK_STREAM)
# socket.socket == creates new socket's object
# socket.AF_INET == specifys socket's protocols family. AF_INET is to IPv4. AF_INTET == IPv6.
# socket.SOCK_STREAM = like AF_INET, is a CONSTANT. Used to TCP flows, one of the main possible flows.
# Resume: mysock configures an object that uses protocols IPv4 and TCP.
mysock.connect( ('data.pr4e.org', 80)) (host, port) # port == door
# ".connect", despite of it being obvius, is the method to estabilish socket's connection.
