import os
from jsonsocket import Client

host = 'localhost'
port = 8888

data = {
    'name': 'Patrick Jane',
    'age': 45,
    'children': ['Susie', 'Mike', 'Philip']
}
client = Client()
response = client.connect(host, port).send(data).recv()