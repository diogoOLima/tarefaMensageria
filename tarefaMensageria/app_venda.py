#!/usr/bin/env python3
import requests
from pprint import pprint

url = "http://10.0.1.2:8080"

vendas = [
    {
        "cliente_id": 1,
        "cartao": "Elo"
    },
    {
        "cliente_id": 1,
        "cartao": "Visa"
    }
    ,
    {
        "cliente_id": 1,
        "cartao": "Visa"
    }
]



for venda in vendas:  
    requests.post(f"{url}/venda", json=venda)

r = requests.get(f"{url}/venda")
pprint(r.json())