import requests
import json

URL = 'http://127.0.0.1:8000/studentcreate/'


data = {
    'name':'Romana',
    'roll':222,
    'city':'Rorisal'
}

json_data = json.dumps(data)

r = requests.post(url=URL, data=json_data)

json_data=r.json()

print(json_data)
