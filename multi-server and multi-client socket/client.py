#!/usr/bin/env python3
__author__ = "Matheus Rocha Vieira"
__version__ = "0.1.0"
__license__ = "GPL-3.0"

import os
import re
from jsonsocket import Client

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

def handleEmail(inputEmailLabel):
	flag = True
	while flag:
		inputEmail = input(inputEmailLabel)
		if(
			re.match(
				r'\b[A-Za-z0-9._+-]+@[A-Za-z0-9.-]+\.[(A-Z|a-z)0-9]{2,}\b', inputEmail
			)
		):
			universityUser = inputEmail.split('@')[0]
			universityDomain = inputEmail.split('@')[1]
			universityName = universityDomain.split('.')[0]
			flag = False
		print("Please insert a valid email")
	return [universityUser, universityName, universityDomain]

	

handleEmail(
	inputEmailLabel='Sur University Email: '
)
host = srvlist[universityName]['ip']
port = srvlist[universityName]['port']

flag = True
while flag:
	emitterEmail = input('Sur University Email: ')
	try:
		emitterDomain = emitterEmail.split('@')[1].split('.')[0]
		emitterUser = emitterEmail.split('@')[0]
		try:
			host = srvlist[emitterDomain]['ip']
			port = srvlist[emitterDomain]['port']
			flag = False
		except:
			print("Error")
	except:
		print("Please insert a valid email")
	

while True:
	client = Client()
	print('HOST: ' + str(host))
	print('PORT: ' + str(port))
	print('DOMAIN: ' + str(emitterDomain))
	print('USER: ' + str(emitterUser))
	print('\nType 1 for Send\nType 2 to Receive')
	menu = input('Option: ')
	if menu == '1':
		recipientEmail = input('Recipient University Email: ')
		recipientDomain = recipientEmail.split('@')[1].split('.')[0]
		recipientUser = recipientEmail.split('@')[0]
		msg = input('Message:')
		data = {
			'act': 'send',
			'recipientDomain': recipientDomain,
			'recipientUser': recipientUser,
			'emitterDomain': emitterDomain,
			'emitterUser': emitterUser,
			'msg': msg
		}
		response = client.connect(host, port).send(data).recv()
		client.close()
		if response['status'] == '200':
			print('Success Sending Msg')
		else:
			print('Msg Send Error')

	if menu == '2':
		data = {
			'act': 'receive',
			'requesterUser': emitterUser
		}
		response = client.connect(host, port).send(data).recv()
		#if response['status'] == '200':
		#	print('There are: ' + response.index() + ' new msg')
		for i in response:
			# print('EMAIL #'+i.index())
			print('Emitter: ' + i['emitterUser'] + '@' + i['emitterDomain'])
			print('Msg: ' + i['msg'])
		else:
			print('No New Msg')
		client.close()
