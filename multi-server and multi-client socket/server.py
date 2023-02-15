#!/usr/bin/env python3
__author__ = "Matheus Rocha Vieira"
__version__ = "0.1.0"
__license__ = "GPL-3.0"

import os
from jsonsocket import Server, Client

srvlist = {
	"ufv":
	{
		"id": 1,
		"ip": 'localhost',
		"port": 8888
	},
	"ufla":
	{
		"id": 2,
		"ip": 'localhost',
		"port": 8889
	}
}

usrList = {""}

serverDomain = input('University: ')
host = srvlist[serverDomain]['ip']
port = srvlist[serverDomain]['port']

server = Server(host, port)

msgList = []

while True:
	print('UNIVERSITY: ' + str(srvlist[serverDomain]['id']))
	print('HOST: ' + str(host))
	print('PORT: ' + str(port))
	data = server.accept().recv()
	print('Msg Memory: ' + str(msgList))
	print('Socket Receive Data: ' + str(data))
	if data['act'] == 'send':
		server.send({'status': '200'})
		if data['recipientDomain'] == serverDomain:
			data['status'] = '202'
			msgList.append(data)
		if data['recipientDomain'] != serverDomain:
			print('Transferring Msg: ' + str(data['recipientDomain']))
			client = Client()
			data['status'] = '201'
			response = client.connect(srvlist[data['recipientDomain']]['ip'], srvlist[data['recipientDomain']]['port']).send(data).recv()
			client.close()
			if response['status'] == '200':
				print('Transfered Msg Success')
			else:
				print('Transfered Msg Error')
	if data['act'] == 'receive':
		requesterMsgList = []
		for i in msgList:
			if i['recipientUser'] == data['requesterUser']:
				requesterMsgList.append(i)
				msgList.remove(i)
		server.send(requesterMsgList)
	if (data['act'] != 'receive') & (data['act'] != 'send'):
		server.send('ação desconhecida')
		print('ação desconhecida')
