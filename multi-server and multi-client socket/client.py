import os
from jsonsocket import Client, Server

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

emitterDomain = input('University:')
emitterUser = input('Sur Username:')
host = srvlist[emitterDomain]['ip']
port = srvlist[emitterDomain]['port']

while True:
	os.system("clear")
	client = Client()
	print('Program Name\nType 1 for Send\nType 2 to Receive')
	menu = input('Option: ')
	if menu == '1':
		recipientUser = input('Recipient User:')
		recipientDomain = input('Recipient University: ')
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
		#print('There are:'+response.index()+'new msg')
		for i in response:
			#print('EMAIL #'+i.index())
			print('Emitter: ' + i['emitterUser'] + '@' + i['emitterDomain'])
			print('Msg: ' + i['msg'])
		else:
			print('No New Msg')
		client.close()
