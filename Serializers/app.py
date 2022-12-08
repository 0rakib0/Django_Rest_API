import requests
import json

URL = 'http://127.0.0.1:8000/studentinfo/3'

data = requests.get(url=URL)
json_data = data.json()

print(json_data)

