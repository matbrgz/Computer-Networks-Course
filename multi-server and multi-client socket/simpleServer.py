import os
from jsonsocket import Server

host = 'localhost'
port = 8888

server = Server(host, port)
while True:
    data = server.accept().recv()
    print('Socket Receive Data: '+str(data))
    server.send({'status': 'ok'})