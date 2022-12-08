import requests
import json


URL = 'http://127.0.0.1:8000/create/'

data = {
    'name':'Foysal',
    'roll':103,
    'city':'Dhaka'
}

json_data = json.dumps(data)

r = requests.post(url=URL, data=json_data)

json_data = r.json()

print(json_data)