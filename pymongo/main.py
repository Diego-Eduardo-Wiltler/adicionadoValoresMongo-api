from pymongo import MongoClient
from pymongo.server_api import ServerApi
import random
from datetime import date, datetime
from tqdm import tqdm
import requests
from fastapi import FastAPI
import pandas as pd


app = FastAPI()

uri = "mongodb://localhost:27017"
client = MongoClient(uri, server_api=ServerApi('1'))
db = client['vendas']
coluna = db['vendas']

data_aleatoria = pd.date_range(start="2000-01-01", end=datetime.today()).to_list()


for _ in tqdm(range(1_000_000)):
    response_nomes = requests.get(f"http://{app.host}:{app.port}/lista_nomes")
    lista_nomes = response_nomes.json()["lista_nomes"]

    response_produtos = requests.get(f"http://{app.host}:{app.port}/lista_produtos")
    lista_produtos = response_produtos.json()["lista_produtos"]
    
    dicio = {
        'cod_venda': random.randint(1, 5000),
        'data_teste': str(random.choice(data_aleatoria)),
        'cod_cliente': random.randint(1, 5000),
        'nome_cliente': random.choice(lista_nomes),
        'cod_produto': random.randint(1, 5000),
        'descricao': random.choice([produto['descricao'] for produto in lista_produtos]),
        'nome_produto': random.choice(lista_produtos),
        'categoria': random.choice([categoria['categoria'] for categoria in lista_produtos]),
        'valor': round(random.uniform(1, 150), 2),
        'qtd': random.randint(1, 11)
    }
   
    coluna.insert_one(dicio)
