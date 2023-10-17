'''
# API RESTful

Representational State Transfer (REST): Transferência Representacional de Estado
Uma API RESTful (também conhecida como API REST) é uma interface de programação de aplicativos (API ou API Web) 
que está em conformidade com as restrições do estilo de arquitetura REST e permite a interação com serviços Web RESTful.
Uma API é um conjunto de definições e protocolos para construir e integrar software de aplicação. 
Às vezes, é chamado de contrato entre um provedor de informações e um usuário de informações – estabelecendo o conteúdo 
exigido do consumidor (a chamada) e o conteúdo exigido pelo produtor (a resposta). Por exemplo, o design da API para 
um serviço meteorológico pode especificar que o usuário forneça um CEP e que o produtor responda com uma resposta em 
duas partes, sendo a primeira a temperatura alta e a segunda a baixa.
Em outras palavras, se você deseja interagir com um computador ou sistema para recuperar informações ou executar uma função, 
uma API o ajuda a comunicar o que deseja a esse sistema para que ele possa entender e atender à solicitação
Você pode pensar em uma API como um mediador entre os usuários ou clientes e os recursos ou serviços da Web que eles desejam obter. 
É também uma forma de uma organização compartilhar recursos e informações enquanto mantém a segurança, o controle e a autenticação — determinando quem tem acesso a quê. 

https://camo.githubusercontent.com/20ddb4d173a5b4844d0ca796470b8bcc853ad6a660eb7c9dcdb08420adfdcee7/68747470733a2f2f75706c6f61642e77696b696d656469612e6f72672f77696b6970656469612f636f6d6d6f6e732f662f66312f526573742d4150492e706e67
'''

# Criando um ambiente virtual para o python: python -m venv ambv
# Ativando o ambiente virtual no Windows: .\ambv\Scripts\activate 
# Ativando o ambiente virtual no Linux: source ambv/bin/activate

'''
# Acessórios

Bibliotecas para Python:
 - fastapi: bibliteca para criar uma API Rest
 - uvicorn: servidor web para subir o FastAPI
'''
# pip install fastapi uvicorn

# Baixando o banco de dados Northwind: https://raw.githubusercontent.com/jpwhite3/northwind-SQLite3/master/dist/northwind.db

# Cria a aplicação principal do FastAPI (app)
from fastapi import FastAPI # cria o serviço de Rest API
import sqlite3 # biblioteca de SQLite
import uvicorn #gestor de aplicação web

# cria a aplicação rest api
app = FastAPI()

# domínio "HOME" da aplicação
# Exemplo: http://127.0.0.1:8000/
@app.get('/')
def home():
    return f'Restfull API da ECAA07 Banco de Dados'

#Criando a rota GET "<url>/produtos" para acessar a lista de produtos.
# Exemplo: http://127.0.0.1:8000/produtos
@app.get('/produtos')
def prod():
    conexao = sqlite3.connect('northwind.db')
    cursor = conexao.cursor()
    cursor.execute("SELECT * FROM Products")
    items = cursor.fetchall()
    conexao.close()
    return items

# Criando a rota GET "<url>/categoria/{item_id}" para acessar uma categoria específica do banco de dados.
# Exemplo: http://127.0.0.1:8000/categoria/2
@app.get('/categorias/{item_id}')
def categ(item_id:int):
    conexao = sqlite3.connect('northwind.db')
    cursor = conexao.cursor()
    cursor.execute("SELECT CategoryName, Description FROM Categories WHERE CategoryID=?",(item_id,))
    items = cursor.fetchall()
    conexao.close()
    return items

# ====== ATIVIDADES ======
# Crie um rota GET "<url>/fornecedor/{pais}" da tabela "Suppliers" para selecionar os fornecedores de um determinado país.
# Exemplo: http://127.0.0.1:8000/fornecedor/USA


# Crie um rota POST "<url>/empregado" da tabela "Employees" enviando os seguintes parâmetros:
# - token_api = "ECAA07"
# - Title ( usar comando LIKE para nomes similares ao enviado)
# Usar Swagger para acessar: http://127.0.0.1:8000/docs




# executa o servidor web
uvicorn.run(app, port=8000)