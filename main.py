import pandas as pd
from flask import Flask, jsonify

# Inicializando o Flask
app = Flask(__name__)


# Construção das funcionalidades
@app.route('/totalvendas')
def totalvendas():
    tabela = pd.read_csv('base-dados/bd.csv')
    total_vendas = tabela['Vendas'].sum()
    resposta = {'total_vendas': total_vendas}
    return jsonify(resposta)


# Rodando a API
app.run()
