# Inserção de dados em MongoDB utilizando Python e FastAPI

Este repositório contém um exemplo de código em Python que utiliza o MongoDB para armazenar dados de vendas de produtos. Além disso, há também uma API criada com o framework FastAPI para fornecer listas de nomes e produtos para o código principal.

## Pré-requisitos
+ Python 3.6 ou superior instalado
+ MongoDB instalado e rodando localmente
+ Pacotes Python: pymongo, tqdm, requests, pandas, fastapi, uvicorn

## Utilização
Para executar o código principal, basta rodar o arquivo main.py:

## python main.py
+ O código irá inserir 1 milhão de vendas aleatórias na coleção vendas do MongoDB. Durante a inserção, o código irá utilizar a API criada no arquivo app.py para obter listas de nomes e produtos.
+ Para acessar a API, basta rodar o arquivo app.py


## Estrutura dos arquivos
1. main.py: código principal que insere as vendas no MongoDB.
2. app.py: código que cria a API com o FastAPI.
3. README.md: arquivo com instruções de utilização do código.

## IMPORTANTE

O arquivo requirements.txt é uma lista de pacotes Python necessários para a execução do código. Ele contém informações sobre as dependências do projeto, especificando as versões dos pacotes a serem instalados.

Para utilizá-lo, basta acessar o diretório do projeto e executar o comando "pip install -r requirements.txt". Dessa forma, o pip irá instalar automaticamente todas as dependências necessárias para a execução do código.

Lembre de entrar dentro de "pymongo" para rodar o projeto, o diretório deve estar direcionando a pasta do venv.
