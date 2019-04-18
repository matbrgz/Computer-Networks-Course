#!/usr/bin/env python3
__author__ = "Matheus Rocha Vieira"
__version__ = "0.0.1"
__license__ = "GPL-3.0"

import socket
import time

ip = "127.0.0.1"
port = 8888

serverAddressPort = (localIP,localPort)
bufferSize = 1024

emitterUser = input('Sur Username:')

UDPClientSocket = socket.socket(socket.AF_INET, socket.SOCK_DGRAM) #criacao objeto UDP
UDPClientSocket.settimeout(1.0) # setando temporizador

print('\t\t\t(@) Cliente')
msgFromClient = input('(#) Digite a mensagem: ') # msg do cliente

start = time.time() # começa a contagem do tempo
UDPClientSocket.sendto(msgFromClient.encode(), serverAddressPort) # manda para o server

try:
    (msgFromServer, address) = UDPClientSocket.recvfrom(bufferSize) # recebe do server
    end = time.time() # finaliza a contagem do tempo
    elapsed = end - start # quando tempo gastou

    print(f'\n(OK) Mensagem enviada em {elapsed} segundos')

    msgFromServer = msgFromServer.decode() # descodifica msg do server
    msgFromServer = format(msgFromServer).upper() # msg em caixa alta

    print("\t(*) Confirmacao do servidor: {}".format(msgFromServer))
except socket.timeout:
    print('ESGOTADO TEMPO LIMITE')

UDPClientSocket.close()
