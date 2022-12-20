#!/usr/bin/env python3
import requests
from pprint import pprint

url = "http://127.0.0.1:8080"

produtos = [
    {"nome": "Macarrão", "preco": 3.50},
    {"nome": "Fósforo", "preco": 0.80},
    {"nome": "Sabonete", "preco": 1.80},
    {"nome": "Sal", "preco": 1.5},
    {"nome": "Farinha", "preco": 3.30},
    {"nome": "Refrigerante", "preco": 4.60}
]

for produto in produtos:  
    requests.post(f"{url}/produto", json=produto)

r = requests.get(f"{url}/produto")
pprint(r.json())