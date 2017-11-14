import requests
import json
response = requests.get('https://viacep.com.br/ws/0/json/')
response.status_code
print(response.json())

