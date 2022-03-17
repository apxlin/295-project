import requests
import time
import json

url = 'http://localhost:30001/request'

payload = dict(
    id = (0, 0),
    client_url = ""
)
payload = {
	'id': (0, 0),
	'client_url': 'http://localhost:20001/reply',
	'timestamp': time.time(),
	'data': 'data_string'
}
headers = {'content-type': 'application/json'}
for i in range(1000):
	r = requests.post(url, data=json.dumps(payload), headers=headers)
